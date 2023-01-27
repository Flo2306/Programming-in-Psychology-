import numpy as np


def prime(n):
    '''
    This function returns all prime numbers within below the value entered as a numpy array.
    An example would be: Input = 8, output = [ 2 3 5 7]. 
    '''
    list_for_primes = list()
    #Creating a list that will be longer than necessary
    for iter in range(2,(n+10)**2):
        for i in range(2,iter):
            if (iter%i==0):
                break
        else:
            list_for_primes.append(iter)
    value_to_return = list_for_primes[:n]
    prime_as_array = np.array(value_to_return)
    return prime_as_array

#Complexity of this solution is horrible as its 0^2 

#2.2.9 
#Keeping some functions seperate from each other makes sense as it allows for easier explanation of what the function does. 
#By having seperate functions, we can adjust the explanations easier and they become easy to interpret. Additionally, 
#maintenance of the functions becomes easier as they are more spread out 

#2.2.10
#I added to further statements checking for the outcome of prime(0) and if the returned values are in a numpy array 

