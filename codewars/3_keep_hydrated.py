import math

hours_cycling_1 = 3
hours_cycling_2 = 6.7
hours_cycling_3 = 11.8

def liters(time):
    return(math.floor(time*0.5))

print(liters(hours_cycling_1))
print(liters(hours_cycling_2))
print(liters(hours_cycling_3))
