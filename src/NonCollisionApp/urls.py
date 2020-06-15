from django.urls import path
from django.contrib import admin
from NonCollisionApp import views as NonCollisionApp_views
urlpatterns = [
    path('page/', NonCollisionApp_views.responseDetails),
    path('responsepage/', NonCollisionApp_views.responseDetails),

]
