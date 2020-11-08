import random
from functions import * 

class Person:
    def __init__(self, age, sex, obesity, diabetes):
        self.age = age
        self.obesity = obesity
        self.sex = sex

class Elder(Person):
    def __init__(self):
        self.age = random.randint(70, 100)
        self.obesity = rand_obesity(0.36)  
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.hbp = HBP(self.age)

class Adult(Person):
    def __init__(self):
        self.age = random.randint(40, 69)
        self.obesity = rand_obesity(0.35)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.hbp = HBP(self.age)        

class YoungAdult(Person):
    def __init__(self):
        self.age = random.randint(20, 39)
        self.obesity = rand_obesity(0.20)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.hbp = HBP(self.age)


class Kid(Person):
    def __init__(self):
        self.age = random.randint(0, 19)
        self.obesity = rand_obesity(0.14)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.hbp = HBP(self.age)


class region():
    def __init__(self, name):
        self.name = name
        self.people = []

    def add(self, person):
        self.people.append(person)

    def info(self):
        t_count = 0
        pop = len(self.people)
        print('Info for', self.name)
        print('Population:', pop)
        for ppl in self.people:
            if ppl.obesity is True:
                t_count += 1
        print(t_count)


        males = 0
        females = 0
        for ppl in self.people:
            if ppl.sex == 'male':
                males += 1
            else:
                females += 1
        print('Males:',males)
        print('Females:',females)

        diabetes = 0
        for ppl in self.people:
            if ppl.diabetes == True:
                diabetes += 1
        print("Fat ass:", diabetes)

        hbp_ppl = 0
        for ppl in self.people:
            if ppl.hbp == True:
                hbp_ppl += 1
        print('Amount of people with hypertension:', hbp_ppl)


if __name__ == "__main__":

    van = region('Vancouver')

    i = 0
    k = 0

    while i < 50:
        id_numb = str(k)
        id_numb = Elder()
        van.add(id_numb)
        i += 1
        k += 1

    van.info()
