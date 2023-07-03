# import math

# # help(math)

# value = 4.35

# print(math.floor(value)) # 4

# print(math.ceil(value)) # 5

# print(round(4.5)) # 4

# print(round(5.5)) # 6

# print(math.pi) # 3.141592653589793

# from math import pi

# print(pi) # 3.141592653589793

# print(math.e) # 2.718281828459045

# print(math.inf) # inf

# print(math.nan) # nan

# print(math.e) # 2.718281828459045

# print(math.log(100, 10)) # 2.0

# print(10 ** 2) # 100

# print(math.sin(10)) # -0.5440211108893698

# print(math.degrees(pi/2)) # 90.0

# print(math.radians(180)) # 3.141592653589793

import random

# print(random.randint(0, 100)) # 77

# random.seed(101) # 101 is the seed value
# print(random.randint(0, 100)) # 74


# print(random.randint(0, 100)) 

mylist = list(range(0, 20))

print(random.choice(mylist)) 

#   Sample with replacement

print (random.choices(population=mylist, k=10)) 

#   Sample without replacement

print (random.sample(population=mylist, k=10))

random.shuffle(mylist)

print(random.uniform(a=0, b=100))

print(random.gauss(mu=0, sigma=1))