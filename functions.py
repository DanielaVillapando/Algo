import random

def rand_sex():
    rand_sex = random.randint(1, 2)
    if rand_sex == 1:
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