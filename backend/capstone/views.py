# from django.shortcuts import render
# import threading
# import time
# from rest_framework.decorators import api_view


# # 2. Computer Vision
# from django.http import HttpResponse, StreamingHttpResponse
# import imutils
# from imutils import face_utils
# import dlib
# import cv2
# import threading

# from scipy.spatial import distance as dist

# # Create your views here.

# @api_view(['GET'])
# def camera_feed(request): 
#     cap = VideoCamera()
#     return StreamingHttpResponse(gen(cap),content_type="multipart/x-mixed-replace;boundary=frame")


#  # EAR calculation function
# def eye_aspect_ratio(eye):
# 	# compute the euclidean distances between the two sets of
# 	# vertical eye landmarks (x, y)-coordinates
# 	A = dist.euclidean(eye[1], eye[5])
# 	B = dist.euclidean(eye[2], eye[4])

# 	# compute the euclidean distance between the horizontal
# 	# eye landmark (x, y)-coordinates
# 	C = dist.euclidean(eye[0], eye[3])

# 	# compute the eye aspect ratio
# 	ear = (A + B) / (2.0 * C)

# 	# return the eye aspect ratio
# 	return ear

# #to capture video class
# class VideoCamera(object):
#     def __init__(self):
#         #create a video capture object
#         #0 refers to the first camera you have (in case multiple cameras available)
        
#         # Video-related
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()

#         # Detection model-related
#         self.hog_face_detector = dlib.get_frontal_face_detector()
#         self.dlib_facelandmark = dlib.shape_predictor("D:/School/SEM 6/CAPSTONE/CapstoneEyes/shape_predictor_68_face_landmarks.dat")
#         (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
#         (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

#         # EAR and blink-related
#         self.EYE_AR_THRESH = 0.25
#         self.EYE_AR_CONSEC_FRAMES = 3
#         self.COUNTER = 0
#         self.TOTAL = 0

#         # Notification-related
#         self.strnotif = ''
#         self.drwnotif = ''
#         self.restnotif = ''
#         self.restcounter = 36000 # 36000 frames = 20 minute
#         self.strain_cnt = 0
#         self.drowsy_cnt = 0
#         self.drowsy_flag = False

#         # Time-related
#         self.start_time = time.time()
#         self.tick = 60 #collect data every 60s (1 minute)

#         # Data capture-related
#         self.last_agg_blink_cnt = self.last_agg_strain_cnt = self.last_agg_drowsy_cnt = 0
#         self.blink_cnt_log = self.strain_cnt_log = self.drowsy_cnt_log = 0

#         threading.Thread(target=self.update, args=()).start()


#     def __del__(self):
#         self.video.release()

#     #function will process every single video frame
#     def get_frame(self):
#         image = self.frame
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         faces = self.hog_face_detector(gray)
#         current_time = time.time()
#         duration = current_time - self.start_time

#         for face in faces:
#             # conversion to NumPy array to work with
#             face_landmarks = face_utils.shape_to_np(self.dlib_facelandmark(gray, face))

#             leftEye = face_landmarks[self.lStart:self.lEnd]
#             rightEye = face_landmarks[self.rStart:self.rEnd]
#             leftEAR = eye_aspect_ratio(leftEye)
#             rightEAR = eye_aspect_ratio(rightEye)
            
#             # average the eye aspect ratio together for both eyes
#             ear = (leftEAR + rightEAR) / 2
            
#             # calculate the convex hull for each eye & visualization for detection of each 
#             leftEyeHull = cv2.convexHull(leftEye)
#             rightEyeHull = cv2.convexHull(rightEye)
#             cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
#             cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)

#             # check to see if the eye aspect ratio is below the blink threshold
#             # if yes -> increment the blink frame counter
#             if ear < self.EYE_AR_THRESH:
#                 self.COUNTER += 1
#             else:
#                 # if the eyes were closed for a sufficient # of frames -> increment the total number of blinks
#                 if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES and self.COUNTER < 12:
#                     self.TOTAL += 1
#                     # reset the eyes-closed frame counter
#                     self.COUNTER = 0
#                 elif self.COUNTER >= 12: #if eyes are closed for longer or equal to 12 frames (roughly 400ms), then it counts as drowsy
#                     self.drowsy_flag = True
            
            
#             # blink rate calculation
#             br = int(60*self.TOTAL/duration)
            
#             # notification system (on-frame)
#             if br > 20:
#                 self.strnotif = 'Your eye is straining'
#                 self.strain_cnt += 1
#             elif br > 15 and br <= 20:
#                 self.strnotif = 'Normal blink rate'
#             elif br > 12 and br <= 15:
#                 self.strnotif = 'Computer blink rate' #still counts as straining
#                 self.strain_cnt += 1

#             #if the eye suffers lower bilnk rate due to computer use for more than 5 minutes (even better, in 5 minutes interval) 
#             # -> alert the user to go get some rest
#                 # 5 minutes = 300 seconds. Considering webcam video is captured at 30fps -> eyes need to strain for 9000 frames
#             if self.strain_cnt % 9000 == 0:
#                 self.strnotif = 'Go get some rest'
            
#             #drowsiness detection
#             if br <= 12:
#                 self.drowsy_cnt += 1 
#                 if self.drowsy_flag == True:
#                     self.drwnotif = 'STOP AND GO TO SLEEP YOU SLEEPYHEAD'
            
#             # 20-20-20 rule enforcement
#             self.restcounter -= 1
#             # after 20', a notification will show up alerting the user to take a rest
#             if self.restcounter == 0:
#                 self.restnotif = 'Take a rest for 20 seconds' #after 20 minutes, shows on screen notification (front end) to 
#                                                                 #alert user to take a rest
#                 self.restcounter = 36000 + +(30 * 20) +(30 * 10) #update restcounter to 20 minutes + + 20s (for user to rest)
#                                                                     # + 10s (for user to respond to prompt)
#             # NOTE TO SELF: reset restnotif after user confirmation

#             # data logging
#             # self.blink_cnt_log = self.TOTAL - self.last_agg_blink_cnt
#             # self.strain_cnt_log = self.strain_cnt - self.last_agg_strain_cnt
#             # self.drowsy_cnt_log = self.drowsy_cnt - self.last_agg_drowsy_cnt
#             # if int(duration) == self.tick:
#             #     self.tick += 60
#             #     serializer = blinkSerializer(data = {\
#             #         "user":Home.current_user,\
#             #         "blink_cnt":self.blink_cnt_log,\
#             #         "blink_rate": br, \
#             #         "drowsy_cnt":int(self.drowsy_cnt_log/30),\
#             #         "strain_cnt":int(self.strain_cnt_log/30)})

#             #     if serializer.is_valid():
#             #         serializer.save()

#             self.last_agg_blink_count = self.TOTAL
#             self.last_agg_strain_cnt = self.strain_cnt
#             self.Last_agg_drowsy_cnt = self.drowsy_cnt
  
#             # draw the total number of blinks on the frame along with
#             # the computed eye aspect ratio for the frame
#             cv2.putText(image, "Blinks: {}".format(self.TOTAL), (10, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             cv2.putText(image, "EAR: {:.2f}".format(ear), (300, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             cv2.putText(image, "Duration: {:.2f}".format(duration), (10, 60),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             cv2.putText(image, "Blink rate: {:.2f}".format(br), (10, 80),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         _, png = cv2.imencode('.png', image)
#         return png.tobytes()

#         # update to a new video frame
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# # generate a video feed by processed frames
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#             b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n\r\n')