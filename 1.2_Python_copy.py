#1.1 

#We needed to import numpy as np for the code to work 
import numpy as np 
another_array = np.zeros((2, 4, 6))
#print(another_array)

#1.2 
#print(another_array[-1,-1,0])
#print(another_array[0, 0, 1])
#print(another_array[1,2,2])


#1.3 

#In Python, the computer points towards the object unlike in R where both the name and the values are considered the same instance. Multiple 
#variables can point to the same object (e.g. a list) which makes it difficult sometimes. Usually, I just copy objects by using the associated copy function 
#e.g. np.copy()
another_array = np.zeros((2, 4, 6)) 
new_array = np.copy(another_array)
new_array[1, 2, 2] = 1 
print(new_array[1, 2, 2])

#1.4 


#1.5 


#1.6 
#pip install pip-install-test

#1.7 
#You can not caluclate the var if you have a nan in the list as it involves a mathematical operation with a value that is "nothing". 
#You can calculate the var if you remove the nan value as it only is ints then 
sample_scores = np.array([1, 6, 7, 8, 9]) 
print(np.var(sample_scores))

#1.8 
example_array = np.full((2,3,4), np.nan)
print(example_array)

#1.9 



#1.10 