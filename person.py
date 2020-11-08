import random
from functions import * 

class Person:
    def __init__(self, age, sex, obesity, diabetes, asthma, hbp):
        self.age = age
        self.obesity = obesity
        self.sex = sex
        self.diabetes = diabetes
        self.asthma = asthma
        self.hbp = hbp

class Elder(Person):
    def __init__(self):
        self.age = random.randint(70, 100)
        self.obesity = rand_obesity(0.36)  
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)

class Adult(Person):
    def __init__(self):
        self.age = random.randint(40, 69)
        self.obesity = rand_obesity(0.35)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)        

class YoungAdult(Person):
    def __init__(self):
        self.age = random.randint(20, 39)
        self.obesity = rand_obesity(0.20)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)


class Kid(Person):
    def __init__(self):
        self.age = random.randint(0, 19)
        self.obesity = rand_obesity(0.14)
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
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
        elder = round(0.113 * pop)
        kid = round(0.224 * pop)
        youngadult = round(0.260 * pop)
        adult = round(0.403 * pop)
        print('Info for', self.name)
        print('Population:', pop)
        print('# of kids:', kid)
        print('# of Young Adults:', youngadult)
        print('# of Adults:', adult)
        print('# of Elders:', elder)

        males = 0
        females = 0
        for ppl in self.people:
            if ppl.sex == 'male':
                males += 1
            else:
                females += 1
        print('Males:',males)
        print('Females:',females)

        for ppl in self.people:
            if ppl.obesity is True:
                t_count += 1
        print("obese:", t_count)

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

        asthma = 0
        for ppl in self.people:
            if ppl.asthma == True:
                asthma += 1
        print("Can't breathe properly:", asthma )


if __name__ == "__main__":

    van = region('Vancouver')

    i = 0
    k = 0

    population = 5100000
    elder = round(0.113 * population)
    kid = round(0.224 * population)
    youngadult = round(0.260 * population)
    adult = round(0.403 * population)

    while elder > 0:
        id_numb = str(k)
        id_numb = Elder()
        van.add(id_numb)
        elder -= 1
        k += 1
    while kid > 0:
        id_numb = str(k)
        id_numb = Kid()
        van.add(id_numb)
        kid -= 1
        k += 1
    while youngadult > 0:
        id_numb = str(k)
        id_numb = YoungAdult()
        van.add(id_numb)
        youngadult -= 1
        k += 1
    while adult > 0:
        id_numb = str(k)
        id_numb = Adult()
        van.add(id_numb)
        adult -= 1
        k += 1

    van.info()
