import random
from operator import attrgetter

""" Sex Function """
''' from our research on StatsCan, BC's population consists of 49.6% Males to 50.6% Females '''
''' rand_sex() function has an if statement that calculates 49.6% Males or else it will return Female '''

def rand_sex():
    rand_sex = random.random()
    if rand_sex <= 0.496:
        return 'male'
    else:
        return 'female'

""" Get Rating Function """
''' function to calculate points for our rating system '''
''' everyone will get points based on their age (age * 0.25) '''
''' if people in mock population has any of the underlying illnesses (obesity, diabetes, asthma, high blood pressure) they will get 15 points '''
''' if the person is working they will get points depending on their job's risk level, healthcare workers are guaranteed to get vaccinated, unemployed people get 0 points '''

def get_rating(age, obesity, diabetes, asthma, hbp, occupation):
    age_rate = age * 0.25
    if obesity == True:
        obesity_rate = 15
    else:
        obesity_rate = 0

    if diabetes == True:
        diabetes_rate = 15
    else:
        diabetes_rate = 0

    if asthma == True:
        asthma_rate = 15
    else:
        asthma_rate = 0

    if hbp == True:
        hbp_rate = 15
    else:
        hbp_rate = 0

    if occupation == "High Risk":
        occupation_rate = 15
    if occupation == "Medium Risk":
        occupation_rate = 10
    if occupation == "Low Risk":
        occupation_rate = 5
    if occupation == "Health Care":
        occupation_rate = 1000
    if occupation == "Unemployed":
        occupation_rate = 0
    score = age_rate + obesity_rate + diabetes_rate + asthma_rate + hbp_rate + occupation_rate
    return score

""" Obesity Function"""
''' function that calculates the obesity rate based on age groups, stats from StatsCan '''
''' EXAMPLE (line 64-68) assigns 14% of people as obese for people between 2 to 18 '''

def rand_obesity(age):
    num = random.random()
    if age < 2:
        return False
    if 2 <= age <= 18:
        if num < 0.14:
            return True
        else:
            return False
    if 18 <= age <= 19:
        if num < 0.15:
            return True
        else:
            return False
    if 20 <= age <= 34:
        if num < 0.18:
            return True
        else:
            return False
    if 35 <= age <= 49:
        if num < 0.31:
            return True
        else:
            return False
    if 50 <= age <= 64:
        if num < 0.31:
            return True
        else:
            return False
    if 65 <= age <= 100:
        if num < 0.33:
            return True
        else:
            return False

""" Diabetes Function """
''' function that calculates people suffering from diabetes based on age groups and sex, stats from StatsCan '''
''' EXAMPLE (line 111-115) assigns 5% of people as obese for males between 35 to 49 '''

def diabetes(sex, age):
    rand_num = random.random()
    if sex == 'male' and 0 <= age < 34:
        if rand_num < 0.01:
            return True
        else:
            return False
    if sex == 'female' and 0 <= age <= 34:
        if rand_num < 0.01:
            return True
        else:
            return False
    if sex == 'male' and 35 <= age <= 49:
        if rand_num < 0.05:
            return True
        else:
            return False
    if sex == 'female' and 35 <= age <= 49:
        if rand_num < 0.04:
            return True
        else:
            return False
    if sex == 'male' and 50 <= age <= 64:
        if rand_num < 0.14:
            return True
        else:
            return False
    if sex == 'female' and 50 <= age <= 64:
        if rand_num < 0.11:
            return True
        else:
            return False
    if sex == 'male' and 65 <= age <= 74:
        if rand_num < 0.21:
            return True
        else:
            return False
    if sex == 'female' and 65 <= age <= 74:
        if rand_num < 0.14:
            return True
        else:
            return False
    if sex == 'male' and 75 <= age <= 100:
        if rand_num < 0.25:
            return True
        else:
            return False
    if sex == 'female' and 75 <= age <= 100:
        if rand_num < 0.16:
            return True
        else:
            return False

""" High Blood Pressure Function """
''' function that calculates people suffering from high blood pressure based on age groups, stats from StatsCan '''
''' EXAMPLE (line 170-174) assigns 9.9% of people with high blood pressure for people between 35 to 49 '''

def HBP(age):
    num = random.random()
    if 0 <= age <= 11:
        return False
    if 12 <= age <= 17:
        if num < 0.004:
            return True
        else:
            return False
    if 18 <= age <= 34:
        if num < 0.021:
            return True
        else:
            return False
    if 35 <= age <= 49:
        if num < 0.099:
            return True
        else:
            return False
    if 50 <= age <= 64:
        if num < 0.253:
            return True
        else:
            return False
    if 65 <= age <= 100:
        if num < 0.435:
            return True
        else:
            return False
    
""" Asthma Function """
''' function that calculates people suffering from asthma based on age groups, stats from StatsCan '''
''' EXAMPLE (line 199-203) assigns 10.9% of people with asthma for people between 18 to 34 '''

def rand_asthma(age):
    rand_asthma = random.random()
    if 0 <= age <= 11:
        return False
    if 12 <= age <= 17:
        if rand_asthma < 0.08:
            return True
        else:
            return False
    if 18 <= age <= 34:
        if rand_asthma < 0.109:
            return True
        else:
            return False
    if 35 <= age <= 49:
        if rand_asthma < 0.078:
            return True
        else:
            return False
    if 50 <= age <= 64:
        if rand_asthma < 0.055:
            return True
        else:
            return False
    if 65 <= age <= 100:
        if rand_asthma < 0.072:
            return True
        else:
            return False

""" Occupation Function """
''' function that calculates occupation distribution of job types in BC's job sector, stats from StatsCan '''
''' assigns High Risk, Medium Risk, and Low Risk based on how risky the job is '''

def rand_occupation(age):
    num = random.random()
    rand_unemployed = random.random()
    if 16 <= age <= 65:
        if rand_unemployed <= .089:
            return "Unemployed"
        else:
            if 0 <= num <= 0.115:
                return "High Risk" # Retail
            if 0.115 < num <= 0.229:
                return "Health Care"
            if 0.229 < num <= 0.321:
                return "Low Risk" # Manufacturing
            if 0.321 < num <= 0.396:
                return "High Risk" # Education
            if 0.396 < num <= 0.469:
                return "Medium Risk" # Public administration
            if 0.469 < num <= 0.54:
                return "Low Risk" # Scientific and Technical Services
            if 0.54 < num <= 0.606:
                return "Medium Risk" # Construction
            if 0.606 < num <= 0.668:
                return "Medium Risk" # Accommodation and Food Services
            if 0.668 < num <= 0.716:
                return "Medium Risk" # Transportation and Warehousing
            if 0.716 < num <= 0.762:
                return "Medium Risk" # Other Services
            if 0.762 < num <= 0.807:
                return "Low Risk" # Finance and Insurance
            if 0.807 < num <= 0.849:
                return "Medium Risk" # Wholesale trade
            if 0.849 < num <= 0.889:
                return "Medium Risk" # Public services
            if 0.889 < num <= .913:
                return "Low Risk" # Agriculture, Forestry, and Fishing/Hunting
            if 0.913 < num <= 0.937:
                return "High Risk" # Information and cultural industries
            if 0.937 < num <= 0.956:
                return "High Risk" # Entertainment
            if 0.956 < num <= 0.975:
                return "Medium Risk" # Real Estate
            if 0.975 < num <= 0.99:
                return "Low Risk" # Mining and Oil
            if 0.99 < num <= 0.999:
                return "Low Risk" # Utilities
            if 0.999 < num <= 1:
                return "Medium Risk" # Management of Companies
    else:
        return "Unemployed"

""" Distribution Function """
''' Distributes vaccines based on the points people get in our mock applicaiton '''
''' people with more points will be given the vaccine first '''
''' prints out the information regarding the vaccinated population '''

def distribution(people, population):
    sortedlist = sorted(people, key=attrgetter('rating'), reverse=True)
    vaccinated_kids = 0
    vaccinated_young_adults = 0
    vaccinated_adults = 0
    vaccinated_elders = 0
    for i in sortedlist:
        if i.vaccinated == False:
            vaccine = input("How many vaccines do we have? or none: ")
            if vaccine == "none":                
                print("Total amount of vaccinated Kids:", vaccinated_kids)
                print("Total amount of vaccinated Young Adults:", vaccinated_young_adults)
                print("Total amount of vaccinated Adults:", vaccinated_adults)
                print("Total amount of vaccinated Elders:", vaccinated_elders)
                print("Population:", population)
                print("Total population vaccinated:", vaccinated_elders + vaccinated_adults + vaccinated_kids + vaccinated_young_adults)
                print("Total population not vaccinated:", population - (vaccinated_elders + vaccinated_adults + vaccinated_kids + vaccinated_young_adults))
                print('')
                break
            vaccine = int(vaccine)

            for i in sortedlist:
                if vaccine !=0 and i.vaccinated == False:
                    if 0 <= i.age <= 19:
                        vaccinated_kids+=1
                        i.vaccinated = True
                    elif 20 <= i.age <=39:
                        vaccinated_young_adults+=1
                        i.vaccinated = True
                    elif 40 <= i.age <= 69:
                        vaccinated_adults+=1
                        i.vaccinated = True
                    elif 70 <= i.age <= 100:
                        vaccinated_elders+=1
                        i.vaccinated = True
                    vaccine-=1
            
            print("Total amount of vaccinated Kids:", vaccinated_kids)
            print("Total amount of vaccinated Young Adults:", vaccinated_young_adults)
            print("Total amount of vaccinated Adults:", vaccinated_adults)
            print("Total amount of vaccinated Elders:", vaccinated_elders)
            print("Population:", population)
            print("Total population vaccinated:", vaccinated_elders + vaccinated_adults + vaccinated_kids + vaccinated_young_adults)
            print("Total population not vaccinated:", population - (vaccinated_elders + vaccinated_adults + vaccinated_kids + vaccinated_young_adults))
            print('')

    arr = []

    for i in sortedlist:
        if (i.vaccinated == False):
            arr.append(False)
        else:
            arr.append(True)
    
    results = all(arr)
    if results == True:
        print('Population Vaccinated')
    else:
        print('Not all population Vaccinated')
