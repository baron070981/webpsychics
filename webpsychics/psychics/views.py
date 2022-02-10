from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpRequest
from  django.contrib.sessions.models import Session

from random import randint

from .models import *
from .forms import *
from .psychicsprocessing import PsychicDataHandler
from .psychicsprocessing import SessionHandler





class PsychicsListView(ListView):
    
    template_name = 'psychics/guess_number_page.html'
    
    
    
    def get_queryset(self):
        session_key = self.request.session.session_key
        self.request.session.set_expiry(60)
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        SessionHandler.create_fields_session(self.request)
        SessionHandler.update_session(self.request)
        return qs
    
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['usernums'] = self.request.session['usernumbers']
        data['psych'] = self.request.session['psychics']
        return data

    
    def post(self, request):
        PsychicDataHandler.answer(self.request)
        return redirect('sendnum')
    


class SendingNumber(ListView):
    
    template_name = 'psychics/number_submission_page.html'

    def get_queryset(self):
        session_key = self.request.session.session_key
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        return qs
    
    
    def get_context_data(self, **kwargs):
        form = SendingNumberForm(self.request.POST)
        data = super().get_context_data(**kwargs)
        data['form'] = form
        data['psych'] = self.request.session['psychics']
        data['usernums'] = self.request.session['usernumbers']
        return data
    
    
    def post(self, request):
        self.form = SendingNumberForm(self.request.POST)
        psychics = self.request.session['psychics']
        num = 0
        if self.form.is_valid():
            num = int(self.form.cleaned_data.get('number'))
            PsychicDataHandler.check_answer(self.request, num)
            PsychicDataHandler.add_number(self.request, num)
            PsychicDataHandler.calculate_psychic_credibility(self.request)
        return redirect('home')









