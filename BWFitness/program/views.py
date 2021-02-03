from django.shortcuts import render
from django.views import generic
from .models import Program
from Exercises.models import Exercise
# Create your views here.

class ProgramList(generic.ListView):
    model = Program

class AddToProgram(generic.TemplateView):
    template_name = 'program/add_to_program.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        myslug = self.kwargs['slug']
        exToAdd = Exercise.objects.get(slug=myslug)
        p = Program(exercise=exToAdd)
        p.save()
        return context


class RemoveFromProgram(generic.TemplateView):
    template_name = 'program/remove_from_program.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        myslug = self.kwargs['slug']
        exToRemove = Exercise.objects.get(slug=myslug)
        Program.objects.get(exercise=exToRemove).delete()
        return context
