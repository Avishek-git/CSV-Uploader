from uploader import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('upload',views.upload_file,name='uploader'),
]

