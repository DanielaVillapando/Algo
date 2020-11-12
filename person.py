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
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)

class Adult(Person):
    def __init__(self):
        self.age = random.randint(40, 69)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)        

class YoungAdult(Person):
    def __init__(self):
        self.age = random.randint(20, 39)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)


class Kid(Person):
    def __init__(self):
        self.age = random.randint(0, 19)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)


class region():
    def __init__(self, name, pop, elder, kid, YA, adult):
        self.name = name
        self.population = pop
        self.elder = elder
        self.kid = kid
        self.YA = YA
        self.adult = adult
        self.people = []

    def add(self, person):
        self.people.append(person)

    def info(self):
        print('Info for', self.name, "\n")
        print('Population:', self.population)
        print('Number of Kids:', self.kid)
        print('Number of Young Adults:', self.YA)
        print('Number of Adults:', self.adult)
        print('Number of Elders:', self.elder, "\n")

        males = 0
        females = 0
        for ppl in self.people:
            if ppl.sex == 'male':
                males += 1
            else:
                females += 1
        print('Males:',males)
        print('Females:',females, "\n")

        obesity = 0
        for ppl in self.people:
            if ppl.obesity is True:
                obesity += 1
        print("Amount of people with obesity:", obesity)
        print("Total percentage of population with obesity: {:.2f}% \n".format(obesity/self.population * 100))

        diabetes = 0
        for ppl in self.people:
            if ppl.diabetes == True:
                diabetes += 1
        print("Amount of people with diabetes:", diabetes)
        print("Total percentage of population with diabetes: {:.2f}% \n".format(diabetes/self.population * 100))

        hbp_ppl = 0
        for ppl in self.people:
            if ppl.hbp == True:
                hbp_ppl += 1
        print('Amount of people with hypertension:', hbp_ppl)
        print("Total percentage of population with hypertension: {:.2f}% \n".format(hbp_ppl/self.population * 100))

        asthma = 0
        for ppl in self.people:
            if ppl.asthma == True:
                asthma += 1
        print("Amount of people with asthma:", asthma )
        print("Total percentage of population with asthma: {:.2f}% \n".format(asthma/self.population * 100))


if __name__ == "__main__":
    population = 5071000
    elder = round(0.113 * population)
    kid = round(0.224 * population)
    young_adult = round(0.260 * population)
    adult = round(0.403 * population)

    BC = region('British Columbia', population, elder, kid, young_adult, adult)

    i = 0
    k = 0


    while elder > 0:
        id_numb = str(k)
        id_numb = Elder()
        BC.add(id_numb)
        elder -= 1
        k += 1
    while kid > 0:
        id_numb = str(k)
        id_numb = Kid()
        BC.add(id_numb)
        kid -= 1
        k += 1
    while young_adult > 0:
        id_numb = str(k)
        id_numb = YoungAdult()
        BC.add(id_numb)
        young_adult -= 1
        k += 1
    while adult > 0:
        id_numb = str(k)
        id_numb = Adult()
        BC.add(id_numb)
        adult -= 1
        k += 1

    BC.info()
