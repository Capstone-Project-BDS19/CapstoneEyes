from django.urls import path
from django.views.generic import TemplateView

app_name = 'capstone'

urlpatterns=[
    path('', TemplateView.as_view(template_name = 'capstone/index.html'))
]