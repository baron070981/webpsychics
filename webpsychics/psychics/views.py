from django.shortcuts import render
from django.http import HttpResponse
from . import utilits
from .utilits import Psychics, psychics_person, psychics_proc

from random import randint

from .forms import SendNumForm




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
state = 1

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
    except Exception as err:
        pass
    person['ratings'] = rating
    return person



def index(request):
    global psychics_person
    global history
    global state
    request.session['state'] = state
    request.session['psychics'] = psychics_person
    request.session['historynum'] = history
    form = SendNumForm()
    
    if request.method == 'POST':
        if state == 1 and request.POST.get('button_setnum'):
            state = 0
            
        elif state == 0:
            form = SendNumForm(request.POST)
            num = 0
            if form.is_valid():
                num = int(form.cleaned_data.get('number'))
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
        'psychics':request.session.get('psychics'),
        'form':form,
    }
        
    
    return render(request, 'psychics/index.html', content)




































    
    
    


