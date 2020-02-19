#Given February 11, 2020

#Using a function rand5() that returns an integer from 1 to 5 (inclusive)
#with uniform probability, implement a function rand7() that returns an
#integer from 1 to 7 (inclusive)

from random import randint

def rand5():
    '''returns an integer from 1 to 5 inclusive with uniform probability
    '''
    return randint(1, 5)

def rand7():
    '''returns an integer from 1 to 7 using rand5()
    '''
    #Explanation:
    #rand5() + rand5() allows us to uniformly get a number between 1 to 10.
    #If we modulo this number by 2, we get either 0 or 1.

    #if we have a uniform chance of getting between 1 and 5
    #and a uniform chance of getting a number between 0 and 1 twice
    #we have a uniform chance of getting a number between 1 and 7
    
    x = (rand5() + rand5()) % 2
    y = (rand5() + rand5()) % 2
    return rand5() + x + y

if __name__ == "__main__":
    for i in range(100):
        a = rand7()
        if a < 1 or a > 7:
            raise Exception
        print(a)
