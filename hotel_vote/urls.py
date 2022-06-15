from django.urls import path
from .views import Hotel_list
from .views import RegisterUserAPIView,LoginView,Daily_Winners_history,vote
from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView

urlpatterns = [
   
    path('hotel',Hotel_list.as_view(),name='hotel'),

    path('hotel/<int:pk>/', Hotel_list.as_view(),name='all'),

    path('register',RegisterUserAPIView.as_view()),
    path('login',LoginView.as_view()),

    path('Daily_Winners_history',Daily_Winners_history.as_view()),

    path('vote/<int:pk>/',vote.as_view()),


   
    
 

] 