from django.shortcuts import render
from django.http import HttpResponse
from . import utilits
from .utilits import Psychics, psychics_person, psychics_proc

from random import randint





psychics_person = {
                'izolda':{'name':'izolda', 
                             'guessed':[], 
                             'ratings':0,
                             'allnums':0,},
                 
                'germogen':{'name':'germogen', 
                             'guessed':[], 
                             'ratings':0,
                             'allnums':0,},
                 
                'svyatozar':{'name':'svyatozar', 
                             'guessed':[], 
                             'ratings':0,
                             'allnums':0,},
                 
                'evlampy':{'name':'evlampy', 
                             'guessed':[], 
                             'ratings':0,
                             'allnums':0,},
            }

history = []

def check_number(compared, person):
    states = [2,3,5,compared]
    statenum = states[randint(0,len(states)-1)]
    if compared % statenum == 0:
        person['guessed'].append(str(compared))
    return person


def rating_calc(len_allnums, person):
    rating = 0
    try:
        rating = int(len(person['guessed'])/len_allnums*100)
        print('In function rating_calc:', rating)
    except Exception as err:
        print('Error:', err)
        pass
    person['ratings'] = rating
    return person


def index(request):
    global psychics_person
    global history
    state = 1
    
    request.session['psychics'] = psychics_person
    request.session['historynum'] = history
    
    if request.method == 'POST':
        
        if request.POST.get('button_setnum'):
            data = request.session.get('psychics')
            request.session['psychics'] = psychics_person
            state = 0
            
        elif request.POST.get('button_sendnum'):
            num = int(request.POST.get('button_sendnum'))
            history = request.session.get('historynum')
            psychics_person = request.session.get('psychics')
            if num >= 10 and num < 100:
                history.append(str(num))
                request.session['historynum'] = history
                for key, person in psychics_person.items():
                    upd_person = check_number(num, person)
                    upd_person = rating_calc(len(history), upd_person)
                    psychics_person[key] = upd_person
                    
                request.session['psychics'] = psychics_person
                state = 1
            else:
                state = 0
        
        
    content = {
        # 'guessed':utilits.psychics_proc.get('guessed'),
        'sendstate':state,
        # 'ratings': psychics_proc.get('rating'),
        'historynum':request.session.get('historynum'),
        'psychics':request.session.get('psychics')
    }
        
    
    return render(request, 'psychics/index.html', content)




































    
    
    


