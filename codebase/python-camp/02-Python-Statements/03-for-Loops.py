lst = [(1,2), (3, 4), (5, 6), (7, 8)]

for a, b in lst:
    print(a)
    print((a, b))

new_lst = [[a for a, b in lst], [b for a, b in lst]]

print(new_lst)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)
    
for item in d.values():
    print(item)
    
for item in d.keys():
    print(item)
    
for item in d.items():
    print(item)
    
for k, v in d.items():
    print((k, v))
    
x_lst = [1, 2, 3]

for item in x_lst:
    ...
    
for item in x_lst:
    pass    

# print('end of script')    

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    # print(letter)
    
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
    
    