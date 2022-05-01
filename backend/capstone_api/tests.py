from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from capstone.models import Post, Category
from django.contrib.auth.models import User

# test if we can actually make a post with our API
class PostTests(APITestCase): 
    def test_view_posts(self): #test if we can view the post
        url = reverse('capstone_api:listcreate')
        response = self.client.get(url, format= 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test if we can creete the post
    def create_post(self):
        self.test_category = Category.objects.create(name ='django')
        self.testuser1= User.objects.create_user(
            username= 'test_user1', password= '123456789')
        data = {"title":"new", 
                "author":1,
                "excerpt": "new",
                "content": "new"}
        url = reverse('capstone_api:listcreate')
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




