from django.urls import path
from . import views

app_name = 'Exercises'

urlpatterns=[
     path('',views.ListExercises.as_view(),name='all'),
     path('<slug:slug>/',views.SingleExercise.as_view(),name='single'),
]
