from django.urls import path
from .views import PostList, PostDetail

app_name = 'capstone_api'


#the below are 2 endpoints, 2 views
# the 1st view takes into the primary key (pk) - to show a single
# component or object in the database

# 2nd view takes into nothing
# it shows all the information in the database

urlpatterns=[
    path('<int:pk>/', PostDetail.as_view(), name = 'detailcreate'),
    path('', PostList.as_view(), name = 'listcreate')
]