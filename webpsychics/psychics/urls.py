from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [

    path('', views.PsychicsListView.as_view(), name='home'),
    path('sendnum', views.SendingNumber.as_view(), name='sendnum'),

]
