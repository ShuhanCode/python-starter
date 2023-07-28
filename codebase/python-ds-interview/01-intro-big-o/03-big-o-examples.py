# O(1) Constant example

def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    print(values[0])
    
func_constant([1,2,3])

# O(n) Linear example

def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print(val)
        
func_lin([1,2,3])

#   O(n^2) Quadratic example

def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print(item_1,item_2)
            
func_quad([1,2,3])

#   Calculating Scale of Big-O

def print_once(lst): # O(n)
    '''
    Prints all items once
    '''
    for val in lst:
        print(val)
        
print_once([1,2,3])

def print_3(lst): # O(3n) --> O(n)
    '''
    Prints all items three times
    '''
    for val in lst:
        print(val)
        
    for val in lst:
        print(val)
        
    for val in lst:
        print(val)
        
print_3([1,2,3])            
                        
def comp(lst): # O(1 + 1/2n + 10) --> O(n)
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print(lst[0])
    
    midpoint = len(lst)//2
    
    for val in lst[:midpoint]:
        print(val)
        
    for x in range(10):
        print('number')
        
print(comp([1,2,3,4,5,6,7,8,9,10]))    

 #  Worst Case vs Best Case
 
def matcher(lst,match): # O(n)
    '''
    Given a list lst, return a boolean indicating if match item is in the list
    '''
    for item in lst:
        if item == match:
            return True
    return False

#   Best case: O(1) --> item is first item in list
#   Worst case: O(n) --> item is not in list or is last item in list

print(matcher([1,2,3,4,5],1))

#   Space Complexity

def printer(n=10): # O(1)
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print('Hello World!')

printer()

def create_list(n): # O(n)
    '''
    Creates a list containing 1 to n
    '''
    new_list = []
    
    for num in range(n):
        new_list.append('new')
        
    return new_list

print(create_list(5))