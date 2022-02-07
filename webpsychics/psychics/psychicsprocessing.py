import copy



class PsychicDataHandler:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def calculate_psychic_credibility(request):
        for name, vals in request.session['psychics'].items():
            numbers = len(vals['numbers'])
            r_answers = len(vals['right_answers'])
            rating = int(r_answers/numbers*100) if numbers > 0 else 0
            request.session['psychics'][name]['rating'] = rating
        request.session.save()
    
    
    @staticmethod
    def check_answer(request, num):
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




















