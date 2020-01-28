"""social_distribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name="Main_Page"),
    path('admin/', admin.site.urls),
    path('posts/', get_public_posts, name="Get-Public_Posts"),
    path('posts/{post_id}/', get_single_post, name="Get_Single_Post"),
    path('author/posts/', auth_posts, name="Auth_Posts"),
    path('author/{author_id}/posts/', get_user_public_posts, name="Get_User_Public_Posts"),
    path('posts/{post_id}/comments/', post_comments, name="Post_Comments"),
    path('author/{author_id}/friends/', friends, name="Friends"),
    path('author/{author1_id}/friends/{author2_id}/', check_friends, name="Check_Friends"),
    path('friendrequest/', friend_request, name="Friend_Request"),
    path('author/{author_id}/', get_author_profile, name="Get_Author_Profile"),
]
