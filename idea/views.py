from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpRequest, HttpResponse

from .forms import IdeaForm

class IdeaView(FormView):
    template_name = 'idea/idea.html'
    form_class = IdeaForm

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)
