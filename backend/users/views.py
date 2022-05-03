from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from users.models import NewUser


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        # else:
        #     try: 
        #         match = NewUser.objects.get(email= serializer.data.email)
        #     except:
        #         return Response(-1)
        #     else: 
        #         return Response("None")
        
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)