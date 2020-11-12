import random

def rand_sex():
    rand_sex = random.random()
    if rand_sex <= 0.496:
        return 'male'
    else:
        return 'female'

def rand_obesity(age):
    num = random.random()
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
    

def rand_asthma(age):
    rand_asthma = random.random()
    if 0 <= age <= 11:
        return False
    if 12 <= age <= 17:
        if rand_asthma < 0.08:
            return True
    if 18 <= age <= 34:
        if rand_asthma < 0.109:
            return True
    if 35 <= age <= 49:
        if rand_asthma < 0.078:
            return True
    if 50 <= age <= 64:
        if rand_asthma < 0.055:
            return True
    if 65 <= age <= 100:
        if rand_asthma < 0.072:
            return True
    else:
        return False


def rand_occupation(age):
    num = random.random()
    rand_unemployed = random.random()
    if 16 <= age <= 65:
        if rand_unemployed <= .089:
            return "Unemployed"
        else:
            if 0 <= num <= 0.115:
                return "Retail"
            if 0.115 < num <= 0.229:
                return "Health Care"
            if 0.229 < num <= 0.321:
                return "Manufacturing"
            if 0.321 < num <= 0.396:
                return "Education"
            if 0.396 < num <= 0.469:
                return "Public Administration"
            if 0.469 < num <= 0.54:
                return "Scientific and Technical Services"
            if 0.54 < num <= 0.606:
                return "Construction"
            if 0.606 < num <= 0.668:
                return "Accommodation and food services"
            if 0.668 < num <= 0.716:
                return "Transportation and Warehousing"
            if 0.716 < num <= 0.762:
                return "Other services"
            if 0.762 < num <= 0.807:
                return "Finance and Insurance"
            if 0.807 < num <= 0.849:
                return "Wholesale trade"
            if 0.849 < num <= 0.889:
                return "Public services"
            if 0.889 < num <= .913:
                return "Agriculture, Forestry, and Fishing/Hunting"
            if 0.913 < num <= 0.937:
                return "Information and cultural industries"
            if 0.937 < num <= 0.956:
                return "Entertainment"
            if 0.956 < num <= 0.975:
                return "Real Estate"
            if 0.975 < num <= 0.99:
                return "Mining and Oil"
            if 0.99 < num <= 0.999:
                return "Utilities"
            if 0.999 < num <= 1:
                return "Management of Companies"
    else:
        return "Unavailable to work"