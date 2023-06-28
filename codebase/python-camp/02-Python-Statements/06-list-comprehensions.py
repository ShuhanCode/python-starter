mystring = 'hello'

mylist = [letter for letter in mystring]

print(mylist)

myset = {letter for letter in mystring}

print(myset)

celcius = [0, 10, 20, 34.5]

fahrenhiet = [((9/5)*temp + 32) for temp in celcius]    

print(fahrenhiet)

result = [x for x in range(0, 11)  if x%2 == 0]

print(result)

result = [x if x%2 == 0 else 'ODD' for x in range(0, 11)]

print(result)

result = [x if x%2 == 0 else ... for x in range(0, 11)]

print(result)

result = [x if x%2 == 0 else '' for x in range(0, 11)]

print(result)

result = [x if x%2 == 0 else None for x in range(0, 11)]

print(result)

mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)
        
print(mylist)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]            

print(mylist)