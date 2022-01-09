from random import randint


class Psychics:
    
    all_sending_nums = []
    
    def __init__(self, name):
        self.name = name
        self.guessed = []
        self.rating = 0
        self.allnums = []
        self.keys = ['name', 'guessed', 'rating', 'allnums']
    
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, Psychics):
            return self.name == other.name
    
    
    def answer(self):
        num = randint(10,99)
        self.allnums.append(num)
        return num
    
    # @property
    def tojson(self):
        return {
            'name':self.name,
            'guessed':self.guessed,
            'rating':self.rating,
            'allnums':self.allnums,
        }
    
    def fromdict(self, data):
        for key in data:
            if key in self.keys:
                if key == 'name':
                    if self.name != data['name']:
                        return
                elif key == 'guessed':
                    self.guessed.append(data['guessed'])
                elif key == 'rating':
                    ...
                elif key == 'allnums':
                    self.allnums.append(data['allnums'])
    
    def set_rating(self):
        try:
            return len(self.guessed)/len(self.allnums)
        except:
            return 0.0
    
    def check_number(self, compared):
        if self.allnums and compared == self.allnums[-1]:
            self.guessed.append(self.allnums[-1])
            return True
        return False
    
    

psychics_person = [
                Psychics('izolda'),
                Psychics('germogen'),
                Psychics('svyatozar'),
                Psychics('evlampy'),
            ]



class PsychicsProc:
    
    def __init__(self):
        pass
    
    def add(self, person_list):
        ...



















