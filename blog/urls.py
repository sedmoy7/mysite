from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', ShowThisPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
]
