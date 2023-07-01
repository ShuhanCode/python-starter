# Collections Module - Counter

from collections import Counter

mylist = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3]

result = Counter(mylist)

print(result) # Counter({1: 13, 2: 4, 3: 4})

Counter('aabsbsbsbhshhbbsbs') # Counter({'b': 7, 's': 6, 'h': 3, 'a': 2})

s = 'How many times does each word show up in this sentence word times each each word'

words = s.lower().split()

result = Counter(words) 

print(result) # Counter({'each': 3, 'word': 3, 'times': 2, 'how': 1, 'many': 1, 'does': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentence': 1})

result.most_common()    # [('each', 3), ('word', 3), ('times', 2), ('how', 1), ('many', 1), ('does', 1), ('show', 1), ('up', 1), ('in', 1), ('this', 1), ('sentence', 1)]

result.most_common(2)   # [('each', 3), ('word', 3)]

list(result)            # ['each', 'word', 'times', 'how', 'many', 'does', 'show', 'up', 'in', 'this', 'sentence']


from collections import defaultdict

# d = {'k1':1}

# d['one'] # KeyError

d  = defaultdict(object)

print(d['one']) # <object at 0x10205d3b0>

for item in d:
    print(item)
    
d = defaultdict(lambda: 0)

d['correct'] = 100

d['Wrong key'] # 0

print(d) # defaultdict(<function <lambda> at 0x10205d488>, {'correct': 100, 'Wrong key': 0})


# namedtuple

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Lab', name='Sammy')

frank = Dog(age=2, breed='Shepard', name="Frankie")

print(sam) # Dog(age=2, breed='Lab', name='Sammy')

print(sam.age) # 2