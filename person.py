import random
from functions import * 
from operator import itemgetter, attrgetter


class Person:
    def __init__(self, age, sex, obesity, diabetes, asthma, hbp, occupation):
        self.age = age
        self.obesity = obesity
        self.sex = sex
        self.diabetes = diabetes
        self.asthma = asthma
        self.hbp = hbp
        self.occupation = occupation
        self.rating = 0

class Elder(Person):
    def __init__(self):
        self.age = random.randint(70, 100)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)
        self.rating = get_rating(self.age, self.obesity, self.diabetes, self.asthma, self.hbp, self.occupation)


class Adult(Person):
    def __init__(self):
        self.age = random.randint(40, 69)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)
        self.rating = get_rating(self.age, self.obesity, self.diabetes, self.asthma, self.hbp, self.occupation)

class YoungAdult(Person):
    def __init__(self):
        self.age = random.randint(20, 39)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)
        self.rating = get_rating(self.age, self.obesity, self.diabetes, self.asthma, self.hbp, self.occupation)



class Kid(Person):
    def __init__(self):
        self.age = random.randint(0, 19) 
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)
        self.rating = get_rating(self.age, self.obesity, self.diabetes, self.asthma, self.hbp, self.occupation)


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
        print("-" * 20)
        print('Info for', self.name)
        print("-" * 20)
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
        print('Females:',females,"\n")

        obesity = 0
        for ppl in self.people:
            if ppl.obesity is True:
                obesity += 1
        print("-" * 20)
        print("Illnesses")
        print("-" * 20)
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
        
        unemployed=0
        unable=0
        HC=0
        high_risk=0
        med_risk=0
        low_risk=0

        for ppl in self.people:
            if ppl.occupation == "Health Care":
                HC += 1
            if ppl.occupation == "High Risk":
                high_risk +=1
            if ppl.occupation == "Medium Risk":
                med_risk +=1
            if ppl.occupation == "Low Risk":
                low_risk +=1
            if ppl.occupation == "Unemployed":
                unemployed +=1
            if ppl.occupation == "Unavailable to work":
                unable +=1

        employed = high_risk + med_risk + low_risk + HC

        print("-" * 20)
        print("Employment Info")
        print("-" * 20)
        print("Amount of people employed:", employed)
        print("Total percentage of population employed: {:.2f}% \n".format(employed/self.population * 100))
        print("Amount of people unable to work:", unable)
        print("Total percentage of population unable to work: {:.2f}% \n".format(unable/self.population * 100))
        print("Amount of people unemployed:", unemployed)
        print("Total percentage of population unemployed: {:.2f}% \n".format(unemployed/self.population * 100))

        print("Amount of people in healthcare:", HC)
        print("Amount of people in high risk jobs:", high_risk)
        print("Amount of people in medium risk jobs:", med_risk)
        print("Amount of people in low risk jobs:", low_risk, "\n")

        vaccine = int(input("How many vaccines do we have? "))
        sortedlist = sorted(self.people, key=attrgetter('rating'), reverse=True)

        vaccinated_kids = 0
        vaccinated_young_adults = 0
        vaccinated_adults = 0
        vaccinated_elders = 0

        for i in sortedlist:
            if vaccine !=0:
                if i.age >= 0 and i.age <= 19:
                    vaccinated_kids+=1
                elif i.age >= 20 and i.age <=39:
                    vaccinated_young_adults+=1
                elif i.age >= 40 and i.age <= 69:
                    vaccinated_adults+=1
                elif i.age >= 70 and i.age <= 100:
                    vaccinated_elders+=1
                vaccine-=1
        
        print("Vaccinated Kids:", vaccinated_kids)
        print("Vaccinated Young Adults:", vaccinated_young_adults)
        print("Vaccinated Adults:", vaccinated_adults)
        print("Vaccinated Elders:", vaccinated_elders)


if __name__ == "__main__":
    population = 50
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

    x = Elder()
    print('I am', x.age, 'with a rating of:', x.rating)