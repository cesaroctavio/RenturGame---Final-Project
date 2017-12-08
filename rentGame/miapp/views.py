# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Usuario , VideoJuego
from django.views.generic.edit import FormView
from .forms import Usuario_form
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView
from  django.http import HttpResponse
from django.core import serializers

# Create your views here.
class Singup(FormView):
    template_name = 'register.html'
    form_class = Usuario_form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = Usuario()
        p.nombre = user
        p.telefono = form.cleaned_data["telefono"]
        p.email = form.cleaned_data["email"]
        p.address = form.cleaned_data["address"]
        p.save()

        return super(Singup,self).form_valid(form)

def index(request):
    videojuegos = VideoJuego.objects.all()
    return render(request,'index.html',{'videojuegos':videojuegos})

class RegistroJuego(CreateView):
    template_name = 'registroJuego.html'
    model = VideoJuego
    fields = '__all__'
    success_url = reverse_lazy('index_view')

class Juego_detail(DetailView):
    template_name = 'detalle_juego.html'
    model = VideoJuego

def jsonVideojuego(request):
    data = serializers.serialize('json',VideoJuego.objects.all())
    return HttpResponse(data, content_type='application/json')
