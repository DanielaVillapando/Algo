import random
from functions import * 

class Person:
    def __init__(self, age, sex, obesity, diabetes, asthma, hbp, occupation):
        self.age = age
        self.obesity = obesity
        self.sex = sex
        self.diabetes = diabetes
        self.asthma = asthma
        self.hbp = hbp
        self.occupation = occupation

class Elder(Person):
    def __init__(self):
        self.age = random.randint(70, 100)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)


class Adult(Person):
    def __init__(self):
        self.age = random.randint(40, 69)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)

class YoungAdult(Person):
    def __init__(self):
        self.age = random.randint(20, 39)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)



class Kid(Person):
    def __init__(self):
        self.age = random.randint(0, 19)
        self.obesity = rand_obesity(self.age) 
        self.sex = rand_sex()
        self.diabetes = diabetes(self.sex, self.age)
        self.asthma = rand_asthma(self.age)
        self.hbp = HBP(self.age)
        self.occupation = rand_occupation(self.age)


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
        retail=0
        HC=0
        manufacturing=0
        education=0
        PA=0
        science=0
        construction=0
        accom_food=0
        transport=0
        other=0
        finance=0
        trade=0
        public_services=0
        agriculture=0
        info_industry=0
        entertainment=0
        real_estate=0
        mining=0
        util=0
        management=0
        unable=0

        for ppl in self.people:
            if ppl.occupation == "Unemployed":
                unemployed +=1
            if ppl.occupation == "Retail":
                retail +=1
            if ppl.occupation == "Health Care":
                HC += 1
            if ppl.occupation == "Manufacturing":
                manufacturing +=1
            if ppl.occupation == "Education":
                education +=1
            if ppl.occupation == "Public Administration":
                PA += 1
            if ppl.occupation == "Scientific and Technical Services":
                science += 1
            if ppl.occupation == "Construction":
                construction += 1
            if ppl.occupation == "Accommodation and food services":
                accom_food +=1
            if ppl.occupation == "Transportation and Warehousing":
                transport += 1
            if ppl.occupation == "Other services":
                other += 1
            if ppl.occupation == "Finance and Insurance":
                finance += 1
            if ppl.occupation == "Wholesale trade":
                trade += 1
            if ppl.occupation == "Public services":
                public_services += 1
            if ppl.occupation == "Agriculture, Forestry, and Fishing/Hunting":
                agriculture +=1
            if ppl.occupation == "Information and cultural industries":
                info_industry += 1
            if ppl.occupation == "Entertainment":
                entertainment +=1
            if ppl.occupation == "Real Estate":
                real_estate += 1
            if ppl.occupation == "Mining and Oil":
                mining +=1
            if ppl.occupation == "Utilities":
                util += 1
            if ppl.occupation == "Management of Companies": 
                management +=1
            if ppl.occupation == "Unavailable to work":
                unable += 1

            employed = retail + HC + manufacturing + education + PA + science + construction + accom_food + transport + other\
             + finance + trade + public_services + agriculture + info_industry + entertainment + real_estate + mining + util + management

        print("-" * 20)
        print("Employment Info")
        print("-" * 20)
        print("Amount of people employed:", employed)
        print("Total percentage of population employed: {:.2f}% \n".format(employed/self.population * 100))
        print("Amount of people unable to work:", unable)
        print("Total percentage of population unable to work: {:.2f}% \n".format(unable/self.population * 100))
        print("Amount of people unemployed:", unemployed)
        print("Total percentage of population unemployed: {:.2f}% \n".format(unemployed/self.population * 100))



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
