class Dog():
    
    species = 'mammal'
    
    def __init__(self, breed, name) -> None:
        self.breed = breed
        self.name = name
        
    def bark(self, number = 1):      
        print('WOOF! My name is {}, number is {}'.format(self.name, number))

my_dog = Dog(breed='Lab', name='Sammy')

print(type(my_dog))  # <class '__main__.Sample'>

print(my_dog.breed)  # Lab

print(my_dog.name)  # Sammy

print(my_dog.species) # mammal

my_dog.bark() # WOOF! My name is Sammy, number is 1

my_dog.bark(10) # WOOF! My name is Sammy, number is 10

#   Circle class

class Circle():
    
    pi = 3.14
    
    def __init__(self, radius = 1) -> None:
        self.radius = radius
        self.area = radius * radius * self.pi
           
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)

print(my_circle.radius) #  30  
print(my_circle.area) # 2826.0

print(my_circle.get_circumference()) # 188.4

#   Inheritance

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")
        
#   Polymorphism

class Dog():
    
    def __init__(self, name) -> None:
        self.name = name
        
    def speak(self):
        return self.name + ' says woof!'
    
class Cat():
    
    def __init__(self, name) -> None:
        self.name = name
        
    def speak(self):
        self.name + ' says meow!'
        
niko = Dog('niko')
felix = Cat('felix')

print(niko.speak()) # niko says woof!

print(felix.speak()) # felix says meow!        
        
for pet in [niko, felix]:
    print(type(pet)) # <class '__main__.Dog'> <class '__main__.Cat'>
    print(type(pet.speak())) # <class 'str'> <class 'NoneType'>   
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko) # niko says woof!

pet_speak(felix) # felix says meow!

class Animal():
        
    def __init__(self, name) -> None:
        self.name = name
        
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')                

#       
# myanimal = Animal('fred')
# myanimal.speak() # NotImplementedError: Subclass must implement this abstract method  

# class Dog(Animal):
     
#      def speak(self):
#          return super().speak() + ' says woof!'
     
# fido = Dog('fido')
# isis = Cat('isis')

# print(fido.speak()) # fido says woof!
# print(isis.speak()) # isis says meow!



#   Special Methods

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")     
        
mybook = Book("Python", "Jose", 100)

print  (mybook) # Title: Python, author: Jose, pages: 100

print (str(mybook)) # 'Title: Python, author: Jose, pages: 100'

print (len(mybook)) # 100

