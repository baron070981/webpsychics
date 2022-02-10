import copy
from random import randint

from .models import *


class PsychicDataHandler:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def calculate_psychic_credibility(request):
        '''
        расчет достоверности отгадок.
        '''
        numbers = len(request.session['usernumbers'])
        for name, vals in request.session['psychics'].items():
            r_answers = len(vals['right_answers'])
            rating = int(r_answers/numbers*100) if numbers > 0 else 0
            request.session['psychics'][name]['rating'] = rating
        request.session.save()
    
    
    @staticmethod
    def check_answer(request, num):
        '''
        проверка верности ответа и добавление в соответствующий список
        '''
        for name, vals in request.session['psychics'].items():
            r_answers = vals['right_answers']
            w_answers = vals['wrong_answers']
            numbers = vals['last_answer']
            print(numbers)
            if num == int(numbers):
                r_answers.append(num)
                request.session['psychics'][name]['right_answers'] = r_answers
            else:
                w_answers.append(num)
                request.session['psychics'][name]['wrong_answers'] = w_answers
        request.session.save()


    @staticmethod
    def add_number(request, number):
        '''
        добавление числа введенного пользователем
        '''
        numbers = request.session['usernumbers']
        numbers.append(number)
        numbers = request.session['usernumbers'] = numbers
        request.session.save()
    
    
    @staticmethod
    def answer(request, start=10, end=99):
        '''
        генерация случайного числа в качестве ответа
        '''
        for key in request.session['psychics']:
            temp_numbers = request.session['psychics'][key]['numbers']
            number = randint(start,end)
            temp_numbers.append(number)
            request.session['psychics'][key]['last_answer'] = number
            request.session['psychics'][key]['numbers'] = temp_numbers
        request.session.save()



class SessionHandler:
    def __init__(self):
        pass
    
    
    @staticmethod
    def create_fields_session(request):
        if 'usernumbers' not in request.session:
            request.session['usernumbers'] = []
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        if 'psychics' not in request.session:
            psychics = {}
            for name in qs:
                psychics[name] = {}
                psychics[name]['rating'] = 0
                psychics[name]['numbers'] = []
                psychics[name]['last_answer'] = 0
                psychics[name]['right_answers'] = []
                psychics[name]['wrong_answers'] = []
            request.session['psychics'] = psychics
        request.session.save()
    
    
    @staticmethod
    def update_session(request):
        
        qs = list(map(lambda x: x.name, PsychicsModel.objects.all()))
        if 'psychics' not in request.session:
            return
        names_in_session = request.session['psychics'].keys()
        if len(names_in_session) > len(qs):
            new_names = list(filter(lambda x: x not in qs, names_in_session))
            for name in new_names:
                del request.session['psychics'][name]
        elif len(names_in_session) < len(qs):
            new_names = list(filter(lambda x: x not in names_in_session, qs))
            for name in new_names:
                request.session['psychics'][name] = {}
                request.session['psychics'][name]['rating'] = 0
                request.session['psychics'][name]['numbers'] = []
                request.session['psychics'][name]['last_answer'] = 0
                request.session['psychics'][name]['right_answers'] = []
                request.session['psychics'][name]['wrong_answers'] = []













