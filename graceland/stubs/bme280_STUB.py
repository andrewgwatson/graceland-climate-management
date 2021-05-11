import random 
def get_temperature():
    # t = random.randrange(-4000, 120000, 1)
    t = random.triangular(-4, 120, 20)
    return t

def get_humidity():
    h = random.triangular(0, 100)
    return h

def get_pressure():
    p = random.triangular(0, 100)
    return p

