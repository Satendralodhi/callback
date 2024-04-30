from django.urls import path
from . import views
urlpatterns = [
   
    path('callback/',views.call_backApi.as_view()),
]