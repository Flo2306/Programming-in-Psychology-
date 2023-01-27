import numpy as np
import datetime
import time
import math 


#2.2.1
#Getting the current time 
#I commented the code as it would run forever otherwise 
'''
#Creating while loop 
while True == 1:
    #getting current time
    now = datetime.datetime.now().hour
    #Checking if current hour is between 1am and 4am 
    if now in range(1,4): 
        print("Go to sleep")
        #Setting system to sleep for 60 minutes to decrease computation necessary. 
        time.sleep(60*60)
    #Similar to what is described above
    elif now in range(8,9):
        print("Eet je hagelslag!")
        time.sleep(60*60)
    else: 
        print("Gut gemacht!")
        time.sleep(60*60)
'''

#2.2.2
#Creating a numeric vector 
numeric_vec = np.random.uniform(low=0, high=100, size=4)
#Setting a sum value 
sum_value = 0

#For loop iterating through numeric vec
for i in range(len(numeric_vec)):
    #Checking if odd or even index 
    if i % 2 == 0:
        #Adding to sum value
        sum_value = sum_value + 2 * numeric_vec[i]
        print(sum_value)
    else: 
        #Adding to sum value
        sum_value = sum_value + numeric_vec[i]
        print(sum_value)

#2.2.3 
grass = "green"
def color_it(color_me, grass_me):
    grass_me = grass
    color_me = "blue"
    colorful_items = np.array([(color_me, grass_me)])
    return colorful_items

sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)

#This returns a UnboundLocalError as the variable grass is used/referenced before it is assigned. This error 
#relates to the variable "grass" being re-assigned a different value in the local function which clashes with the 
#global value. 

#We can fix this by removing grass from the code. As re-assigning grass in the function does not add anything to the function
#this should work fine:) 

#2.2.4 

#Creating input array to try out 
array_random = np.array([1,2,3,4,5,1])

def special(input_array):
    #Checking if input is indeed an array 
    if isinstance(input_array, np.ndarray):
        list_of_values = list()
        Similar_value = 0 
        for value in input_array:
            #If value is not already in the list_of_values it is added, otherwise it is not added and a value 
            #indicating if the list is completely unique is set to 1 
            if value in list_of_values:
                Similar_value = 1
            else: 
                list_of_values.append(value)
        #If no similar values are in the input_array, this value stays 0 so the Warning is raised         
        if Similar_value == 0: 
            raise Warning("All values are special!")
        return list_of_values
    else: 
        raise Exception("Input is not a Numpy Array")

print(special(array_random))

#2.2.5 

class MyClass:
    """A simple example class"""
    classnum = 12345
    def famous(self):
        return 'hello world'


new_stuff = MyClass()
new_stuff.classnum
new_stuff.famous()

#Python classes allow to create basic values/types. Examples of classes are list, np.array, pd.DataFrame etc. It is essentially 
#a blueprint of how to create a certain object like how there are specific ways to create lists and interact with them. 

# Complex number class
class ComplexNum:
    """Creates a complex number"""
    numtype = 'complex'
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def vec_length(self):
        return np.sqrt(self.r**2 + self.i**2)

    def phase_angle(self):
        #I return both alpha and beta as you did not state which one you wanted. 
        #Calculating the angles using formulas I found online and converting them from radians to degree 
        alpha = math.atan(self.i / self.r)* (180/math.pi)
        beta = 180 - 90 - alpha
        return (alpha, beta)


my_num = ComplexNum(3.0, 4.0)
print(my_num)
print((my_num.r, my_num.i))
print(my_num.numtype)
print(my_num.vec_length())
print(my_num.phase_angle())

#2.2.6 
#I was unable to figure a valid solution here but included a sample function so I could do 2.2.7 
def nthpower(N, P):
    if P == 0:
        return 1
    # Recurrence relation
    return (N*nthpower(N, P-1))



#2.2.7 
#Setting the start time
start_time = time.perf_counter()
#Calculating the nthpower
value = nthpower(5,3)   
#End time 
end_time = time.perf_counter()
#Calculating time passed 
time_to_calculate = end_time - start_time
print(value)

#Similar to above just using the absolute values instead 
start_time_1 = time.perf_counter()
value_1 = 4 ** 2
end_time_1 = time.perf_counter()
time_to_calculate_1 = end_time - start_time

print(f'The time to calculate the nthpower with the function is: {time_to_calculate}')
print(f'The time to calculate the nthpower with Python is: {time_to_calculate_1}')

