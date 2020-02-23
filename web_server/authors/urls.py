from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.post_creation_and_retrival_to_curr_auth_user),
    path('<str:author_id>/posts/',
         views.retrieve_posts_of_author_id_visible_to_current_auth_user),
    path('<str:author_id>/friends/',
         views.friend_checking_and_retrieval_of_author_id),
    path('<str:author1_id>/friends/<str:author2_id>/',
         views.check_if_two_authors_are_friends),
    path('<str:author_id>/', views.retrieve_author_profile),
    path('<str:author_id>/update', views.update_author_profile),
    path('unfriend', views.unfriend),
    path('<str:author_id>/addfriend',
         views.view_list_of_available_authors_to_befriend)

]
