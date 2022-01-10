from random import randint
import rich

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
    
    
    def tojson(self):
        return {
            'name':self.name,
            'guessed':self.guessed,
            'rating':self.rating,
            'allnums':self.allnums,
        }
    
    
    def set_rating(self):
        try:
            self.rating = int(len(self.guessed)/len(self.allnums)*100)
            return self.rating
        except:
            self.rating = 0.0
            return 0.0
    
    
    def check_number(self, compared):
        states = [2,3,5,compared]
        statenum = states[randint(0,len(states)-1)]
        self.allnums.append(compared)
        if compared % statenum == 0:
            self.guessed.append(compared)
            return True
        return False
    
    




class PsychicsProc:
    
    params = ['name', 'guessed', 'rating', 'allnums', ]
    
    def __init__(self):
        self.persons = dict()
    
    def add(self, *persons):
        for pers in persons:
            if isinstance(pers, Psychics):
                self.persons[pers.name] = pers
    
    def get(self, param):
        params = {}
        if self.persons:
            for key in self.persons:
                if param == 'guessed':
                    params[key] = self.persons[key].guessed
                elif param == 'rating':
                    params[key] = self.persons[key].rating
        return params
    
    
    def tojson(self):
        persons = {}
        if self.persons:
            for key in self.persons:
                persons[key] = self.persons[key].tojson()
        return persons
    
    


psychics_person = [
                Psychics('izolda'),
                Psychics('germogen'),
                Psychics('svyatozar'),
                Psychics('evlampy'),
            ]


psychics_proc = PsychicsProc()
psychics_proc.add(*psychics_person)












