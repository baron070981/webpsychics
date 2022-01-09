from django.shortcuts import render
from django.http import HttpResponse
from . import utilits

import rich

# Create your views here.

def index(request):
    
    request.session['numbers'] = []
    
    request.session['guessed_nums'] = list(map(
                                            utilits.Psychics.tojson, 
                                            utilits.psychics_person
                                        ))
    
    state = 1
    good_iz = []
    
    
    if request.method == 'POST':
        
        if request.POST.get('button_setnum'):
            data = request.session.get('guessed_nums')
            for person in utilits.psychics_person:
                person.answer()
            
            request.session['guessed_nums'] = list(map(
                                                    utilits.Psychics.tojson, 
                                                    utilits.psychics_person
                                                ))
            rich.print(request.session.get('guessed_nums'))
            state = 0
            
        elif request.POST.get('button_sendnum'):
            num = int(request.POST.get('button_sendnum'))
            if num >= 10 and num < 100:
                utilits.Psychics.all_sending_nums.append(num)
                request.session['numbers'] = utilits.Psychics.all_sending_nums
                for person in utilits.psychics_person:
                    person.check_number(num)
                    person.set_rating()
                request.session['guessed_nums'] = list(map(
                                            utilits.Psychics.tojson, 
                                            utilits.psychics_person
                                        ))
                state = 1
            else:
                state = 0
        
        
        content = {
            'val':[1,2,3,4,5,6], 
            'sendstate':state,
            'ratings': {'izolda':list(filter(lambda x: x == 'izolda', utilits.psychics_person))[0].rating},
            'history_num':utilits.Psychics.all_sending_nums,
        }
        
    
    return render(request, 'psychics/index.html', content)




    
    
    


