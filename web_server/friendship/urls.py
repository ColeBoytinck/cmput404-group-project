from django.urls import path
from . import views
urlpatterns = [
   path('', views.send_friend_request)
]