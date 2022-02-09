import copy
from random import randint


class PsychicDataHandler:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def calculate_psychic_credibility(request):
        '''
        расчет достоверности отгадок.
        '''
        for name, vals in request.session['psychics'].items():
            numbers = len(vals['numbers'])
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
            numbers = vals['numbers']
            if num == int(numbers[-1]):
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
        numbers = request.session['psychics']['allnumbers']
        numbers.append(number)
        numbers = request.session['allnumbers'] = numbers
        request.session.save()
    
    
    @staticmethod
    def answer(request, start=10, end=99):
        '''
        генерация случайного числа в качестве ответа
        '''
        for key in request.session['psychics']:
            temp_numbers = request.session['psychics'][key]['numbers']
            temp_numbers.append(randint(10,99))
            request.session['psychics'][key]['numbers'] = temp_numbers
        request.session.save()

















