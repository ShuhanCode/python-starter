try:
    f = open('testfile','r')
    f.write('Wrie a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')
finally:
    print('I always run')
    
    
def ask_for_int():
    
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('I am going to ask you again! \n')
        
ask_for_int()