from django.shortcuts import render
from django.http import HttpResponse
from . import utilits
from .utilits import Psychics, psychics_person, psychics_proc


# Create your views here.

def index(request):
    
    state = 1
    
    request.session['psychics'] = list(map(
                                            utilits.Psychics.tojson, 
                                            utilits.psychics_person
                                        ))
    
    if request.method == 'POST':
        
        if request.POST.get('button_setnum'):
            data = request.session.get('psychics')
            
            request.session['psychics'] = list(map(
                                                    utilits.Psychics.tojson, 
                                                    utilits.psychics_person
                                                ))
            state = 0
            
        elif request.POST.get('button_sendnum'):
            num = int(request.POST.get('button_sendnum'))
            if num >= 10 and num < 100:
                utilits.Psychics.all_sending_nums.append(num)
                request.session['numbers'] = utilits.Psychics.all_sending_nums
                for person in utilits.psychics_person:
                    person.check_number(num)
                    person.set_rating()
                request.session['psychics'] = list(map(
                                            utilits.Psychics.tojson, 
                                            utilits.psychics_person
                                        ))
                state = 1
            else:
                state = 0
        
        
    content = {
        'guessed':utilits.psychics_proc.get('guessed'),
        'sendstate':state,
        'ratings': psychics_proc.get('rating'),
        'historynum':utilits.Psychics.all_sending_nums,
    }
        
    
    return render(request, 'psychics/index.html', content)




    
    
    


