# Part one
"""
The regular expressions part one
"""

"""
text = "The agent's phone number is 408-555-1234. Call soon!"

print('phone' in text) # True

import re

pattern = 'phone'

match = re.search(pattern, text)

print(match) # <re.Match object; span=(12, 17), match='phone'>   
print(match.span()) # (12, 17)
print(match.start()) # 12
print(match.end()) # 17 

text = "my phone once, my phone twice"

match = re.search(pattern, text)

print(match)  # <re.Match object; span=(3, 8), match='phone'>
print(match.span()) # (3, 8)
print(match.start()) # 3
print(match.end()) # 8 

matches = re.findall(pattern, text)

print(matches) # ['phone', 'phone']

for match in re.finditer('phone', text):
    print(match) # <re.Match object; span=(3, 8), match='phone'> <re.Match object; span=(18, 23), match='phone'>
    print(match.span()) # (3, 8) (18, 23)
    print(match.group()) # phone phone
    
    

# patter = 'NOT IN TEXT'

# print(re.search(pattern, text)) # None

"""

# Part two

import re

text = "My phone number is 408-555-7777"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

print(phone) # <re.Match object; span=(19, 31), match='408-555-7777'>
print(phone.group()) # 408-555-7777

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

print(phone) # <re.Match object; span=(19, 31), match='408-555-7777'>
print(phone.group()) # 408-555-7777


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  

results = re.search(phone_pattern, text)    

print(results) # <re.Match object; span=(19, 31), match='408-555-7777'>

print(results.group()) # 408-555-7777

print(results.group(1)) # 408

# Part three

results = re.search(r'cat|dog', 'The cat is here')

print(results) # <re.Match object; span=(4, 7), match='cat'>

results = re.findall(r'at', 'The cat in the hat sat there.')

print(results) # ['at', 'at', 'at']

results = re.findall(r'.at', 'The cat in the hat went splat.')

print(results) # ['cat', 'hat', 'lat']

results = re.findall(r'...at', 'The cat in the hat went splat.')

print(results) # ['e cat', 'e hat', 'splat']

results = re.findall(r'^\d', '1 is a number')   

print(results) # ['1']  

results = re.findall(r'\d$', 'the number is 4')   

print(results) # ['4']


phrase = 'there are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]+'

results = re.findall(pattern, phrase) 

print(results) #    ['there are ', ' numbers ', ' inside ', ' this sentence']

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

results = re.findall(r'[^!.?]+', test_phrase) 

print(results) # ['This is a string', ' But it has punctuation', ' How can we remove it']

results = re.findall(r'[^!.? ]+', test_phrase) 

print(results) # ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']

print(' '.join(results)) # This is a string But it has punctuation How can we remove it


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'

pattern = r'[\w]+'

print(re.findall(pattern, text)) # ['Only', 'find', 'the', 'hypen', 'words', 'in', 'this', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'long', 'ish', 'they', 'are']

pattern = r'[\w]+-[\w]+'

print(re.findall(pattern, text)) # ['hypen-words', 'long-ish']

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

results = re.search(r'cat(fish|nap|claw)', text)    

