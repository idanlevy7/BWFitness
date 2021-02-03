from django.shortcuts import render
from . import models
from django.views import generic
from . import forms
from program.models import Program
# Create your views here.


class ListExercises(generic.ListView):
    model = models.Exercise

class SingleExercise(generic.DetailView):
    model = models.Exercise

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        info = Program.objects.all()
        context['ex_list']=[]
        for item in info:
            context['ex_list'].append(item.exercise.name)
        return context
