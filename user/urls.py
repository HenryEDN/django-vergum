from django.urls import path
from . import views


urlpatterns = [
    path('User/Login', view=views.loginUser, name='login'),
    path('User/Registration', view=views.registerUser, name='registration'),
    path('User/Logout', view=views.logoutUser, name='logout'),
    path('User/Profile/<int:user_id>', view=views.profileUser, name='profile'),
    path('User/Profile/Update/<int:user_id>', view=views.editProfileUser, name='editProfileUser'),
]
