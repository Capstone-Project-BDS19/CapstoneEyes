from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# include is used to include different path files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('capstone.urls', namespace = 'capstone')),
    path('api/', include('capstone_api.urls', namespace = 'capstone_api')),
    path('api/user/', include('users.urls', namespace = 'users')), #need test
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
