from django.urls import path
from .views import CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),]
    #path('', UserList.as_view(), name = 'list_user')]