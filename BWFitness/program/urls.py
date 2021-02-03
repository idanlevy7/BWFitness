from django.urls import path
from . import views

app_name = 'program'

urlpatterns=[
     path('',views.ProgramList.as_view(),name='my_program'),
     path('add/<slug:slug>/',views.AddToProgram.as_view(),name='add'),
     path('remove/<slug:slug>/',views.RemoveFromProgram.as_view(),name='remove'),
]
