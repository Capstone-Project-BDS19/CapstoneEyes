# 1. Important packages & directories
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blinkapp.models import blnk
from .serializer import *
# 2. Computer Vision
from django.http import HttpResponse, StreamingHttpResponse
from imutils import face_utils
import dlib
import cv2
import threading
# 3. Analysis
from scipy.spatial import distance as dist #calculate Euclidean distance between vertical & horizontal indices to calculate EAR
from scipy.stats import linregress #calculate linear regression slope for measurements
import time #used to calculate duration of model operating to calculate blink rate
from statistics import *
import numpy as np
import datetime

# Create your views here.

# Sign up
# uses the built in usercreationform to help the user sign up an account
# when signed up successfully, it uses the reverse_lazy function to go back the urls.py file to find the specified url details, login form
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# viewing all existing data in data model in JSON format
@api_view(['GET'])
def getData(request):
    item = blnk.objects.all()
    serializer = blinkSerializer(item, many = True)
    return Response(serializer.data)

# demo adding data in JSON format to data model
@api_view(['POST'])
def addItem(request):
    serializer = blinkSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Main function to display to user
def Home(request):
    Home.current_user = request.user.username
    cap = VideoCamera()
    return StreamingHttpResponse(gen(cap),content_type='multipart/x-mixed-replace; boundary=frame')
    #return render(TOTAL)

 # EAR calculation function
def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear

#to capture video class
class VideoCamera(object):
    def __init__(self):
        # Video-related
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()

        # Detection model-related
        self.hog_face_detector = dlib.get_frontal_face_detector()
        self.dlib_facelandmark = dlib.shape_predictor("D:/Study/Uni/1. Capstone II/PyCharm Codes/shape_predictor_68_face_landmarks.dat")
        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        # EAR and blink-related
        self.EYE_AR_THRESH = 0.25
        self.EYE_AR_CONSEC_FRAMES = 3
        self.COUNTER = 0
        self.TOTAL = 0

        # Notification-related
        self.strnotif = ''
        self.drwnotif = ''
        self.restnotif = ''
        self.restcounter = 36000 # 36000 frames = 20 minute
        self.strain_cnt = 0
        self.drowsy_cnt = 0
        self.drowsy_flag = False

        # Time-related
        self.start_time = time.time()
        self.tick = 60 #collect data every 60s (1 minute)

        # Data capture-related
        self.last_agg_strain_cnt = self.last_agg_drowsy_cnt = 0
        self.strain_cnt_log = self.drowsy_cnt_log = 0

        threading.Thread(target=self.update, args=()).start()

    # stop video capture stream
    def __del__(self):
        self.video.release()

    #function will process every single video frame
    def get_frame(self):
        image = self.frame
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.hog_face_detector(gray)
        current_time = time.time()
        duration = current_time - self.start_time

        

        for face in faces:
            # conversion to NumPy array to work with
            face_landmarks = face_utils.shape_to_np(self.dlib_facelandmark(gray, face))

            leftEye = face_landmarks[self.lStart:self.lEnd]
            rightEye = face_landmarks[self.rStart:self.rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            
            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2
            
            # calculate the convex hull for each eye & visualization for detection of each 
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)

            # check to see if the eye aspect ratio is below the blink threshold
            # if yes -> increment the blink frame counter
            if ear < self.EYE_AR_THRESH:
                self.COUNTER += 1
            else:
                # if the eyes were closed for a sufficient # of frames -> increment the total number of blinks
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES and self.COUNTER < 12:
                    self.TOTAL += 1
                    # reset the eyes-closed frame counter
                    self.COUNTER = 0
                elif self.COUNTER >= 12: #if eyes are closed for longer or equal to 12 frames (roughly 400ms), then it counts as drowsy
                    self.drowsy_flag = True
            
            
            # blink rate calculation
            br = int(60*self.TOTAL/duration)
            
            # notification system (on-frame)
            if br > 20:
                self.strnotif = 'Your eye is straining'
                self.strain_cnt += 1
            elif br > 15 and br <= 20:
                self.strnotif = 'Normal blink rate'
            elif br > 12 and br <= 15:
                self.strnotif = 'Computer blink rate' #still counts as straining
                self.strain_cnt += 1

            #if the eye suffers lower bilnk rate due to computer use for more than 5 minutes (even better, in 5 minutes interval) 
            # -> alert the user to go get some rest
                # 5 minutes = 300 seconds. Considering webcam video is captured at 30fps -> eyes need to strain for 9000 frames
            if self.strain_cnt % 9000 == 0:
                self.strnotif = 'Go get some rest'
            
            #drowsiness detection
            if br <= 12:
                self.drowsy_cnt += 1 
                if self.drowsy_flag == True:
                    self.drwnotif = 'STOP AND GO TO SLEEP YOU SLEEPYHEAD'
            
            # 20-20-20 rule enforcement
            self.restcounter -= 1
            # after 20', a notification will show up alerting the user to take a rest
            if self.restcounter == 0:
                self.restnotif = 'Take a rest for 20 seconds' #after 20 minutes, shows on screen notification (front end) to 
                                                                #alert user to take a rest
                self.restcounter = 36000 + +(30 * 20) +(30 * 10) #update restcounter to 20 minutes + + 20s (for user to rest)
                                                                    # + 10s (for user to respond to prompt)
            # NOTE TO SELF: reset restnotif after user confirmation

            # data logging
            self.strain_cnt_log = self.strain_cnt - self.last_agg_strain_cnt
            self.drowsy_cnt_log = self.drowsy_cnt - self.last_agg_drowsy_cnt
            if int(duration) == self.tick:
                self.tick += 60
                serializer = blinkSerializer(data = {\
                    "user":Home.current_user,\
                    "blink_rate": br, \
                    "drowsy_cnt":int(self.drowsy_cnt_log/30),\
                    "strain_cnt":int(self.strain_cnt_log/30)})

                if serializer.is_valid():
                    serializer.save()
            self.last_agg_strain_cnt = self.strain_cnt
            self.Last_agg_drowsy_cnt = self.drowsy_cnt
  
            # draw the total number of blinks on the frame along with
            # the computed eye aspect ratio for the frame
            cv2.putText(image, "Blinks: {}".format(self.TOTAL), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(image, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(image, "Duration: {:.2f}".format(duration), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(image, "Blink rate: {:.2f}".format(br), (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        _, png = cv2.imencode('.png', image)
        return png.tobytes()

    # update to a new video frame
    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

# generate a video feed by processed frames
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n\r\n')
    

# Statistics
def stats(request):
    #specific data retrieveal for logged-in user & date
    data = blnk.objects.filter(user=request.user.username)
    curdate = datetime.date.today()

    #get data for each column as a list
    blink_rate = list(data.values_list('blink_rate', flat = True))
    strain_cnt = list(data.values_list('strain_cnt', flat = True))
    drowsy_cnt = list(data.values_list('drowsy_cnt', flat = True))
    time = list(data.values_list('time', flat = True).filter(date=curdate))
    # calculating statistics to display to user
        #1. mean
    mean_strain_cnt = np.mean(strain_cnt)
    mean_drowsy_cnt = np.mean(drowsy_cnt)

        #2.generating aggregated list for visualization
    agg_blink_rate = np.cumsum(blink_rate)
    agg_strain_cnt = np.cumsum(strain_cnt)
    agg_drowsy_cnt = np.cumsum(drowsy_cnt)
    

        #3. slope (can be understood by the user as how quickly is that measurement increasing)
    """ slope_blink_cnt = linregress(x = time, y = graph_blink_cnt)[0] """

    strain_dur = 0
    for i in range(len(strain_cnt)):
        if strain_cnt[i] >= 30:
            strain_dur += 1
    
    drowsy_dur = 0
    for i in range(len(drowsy_cnt)):
        if drowsy_cnt[i] >= 30:
            drowsy_dur += 1

    date = datetime.date(1, 1, 1)
    datetime1 = datetime.datetime.combine(date, time[0])
    datetime2 = datetime.datetime.combine(date, time[-1])

    used_dur = datetime2 - datetime1
    result = 'Latest blink rate: {}\
         \n Aggregated blink rate: {}\
         \n Strain duration: {} minutes\
         \n Drowsy duration: {} minutes\
         \n Used duration: {}'\
         .format(blink_rate[-1], agg_blink_rate, strain_dur, drowsy_dur, used_dur)
    return HttpResponse(result)