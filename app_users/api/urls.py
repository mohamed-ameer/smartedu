from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignupView.as_view()),#post 
    path('login/',CustomAuthToken.as_view(), name='auth-token'),#post
    path('logout/', LogoutView.as_view(), name='logout-view'),#post

]
