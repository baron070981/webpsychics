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





class PsychicsListView(ListView):
    
    template_name = 'psychics/guess_number_page.html'
    
    
    def create_objects(self):
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        if 'psychics' not in self.request.session:
            psychics = {}
            for name in qs:
                psychics[str(name)] = {}
                psychics[str(name)]['rating'] = 0
                psychics[str(name)]['numbers'] = []
                psychics[str(name)]['right_answers'] = []
                psychics[str(name)]['wrong_answers'] = []
            self.request.session['psychics'] = psychics
    
    
    def upd_psychic(self):
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        if 'psychics' not in self.request.session:
            return
        names_in_session = self.request.session['psychics'].keys()
        print(names_in_session)
        if len(names_in_session) > len(qs):
            new_names = list(filter(lambda x: x not in qs, names_in_session))
            for name in new_names:
                del self.request.session['psychics'][name]
        elif len(names_in_session) < len(qs):
            new_names = list(filter(lambda x: x not in names_in_session, qs))
            for name in new_names:
                self.request.session['psychics'][name] = {}
                self.request.session['psychics'][str(name)]['rating'] = 0
                self.request.session['psychics'][str(name)]['numbers'] = []
    
    
    def get_queryset(self):
        session_key = self.request.session.session_key
        keys = list(map(str, Session.objects.only('session_key')))
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        self.create_objects()
        self.upd_psychic()
        return qs
    
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['psych'] = self.request.session['psychics']
        return data

    
    def post(self, request):
        for key in self.request.session['psychics']:
            temp_numbers = self.request.session['psychics'][key]['numbers']
            temp_numbers.append(randint(10,99))
            self.request.session['psychics'][key]['numbers'] = temp_numbers
            # self.clear_data()
        self.request.session.save()
        return redirect('sendnum')
    
    
    def clear_data(self):
        for name in self.request.session['psychics']:
            self.request.session['psychics'][name]['numbers'] = []
            self.request.session['psychics'][name]['right_answers']
            self.request.session['psychics'][name]['wrong_answers']
        self.request.session.save()


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
        return data
    
    def post(self, request):
        self.form = SendingNumberForm(self.request.POST)
        psychics = self.request.session['psychics']
        num = 0
        if self.form.is_valid():
            num = int(self.form.cleaned_data.get('number'))
            PsychicDataHandler.check_answer(self.request, num)
            PsychicDataHandler.calculate_psychic_credibility(self.request)
        return redirect('home')









