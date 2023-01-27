import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_random():
    random.seed(12172812)
    random_list = np.random.uniform(low = -10, high = 10, size = 100)
    plt.boxplot(random_list)
    plt.show()

    sns.violinplot(random_list)
    sns.stripplot(random_list, jitter = True, color = "White")
    plt.show()

#I think that the second plot is a bit more informative as it is quite similar but still
#shows more things.

#3.2.2
def plot_titanic():
    titanic_data = pd.read_csv("https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv")

    titanic_data.groupby(["Survived", "Pclass"]).size()\
        .plot(kind='bar', title = "Showing classes and number of people survived on the Titanic")
    plt.show()

#3.2.3

def plot_money(): 
        
    data_seaborn_money = sns.load_dataset("tips")

    sns.regplot(data = data_seaborn_money, x = "total_bill", y = "tip")\
    .set(title = "Total bill and tip in a regression plot", )
    plt.xlabel("Total Bill", weight = "bold", size = 20)
    plt.ylabel("Tip", weight = "bold", size = 20)
    plt.show()

#3.2.4
def plot_diamonds(): 
    #The y-axis is slightly off but I was running short on time
    data_seaborn_diamonds = sns.load_dataset("diamonds")
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False)
    correlation_plot_diamonds = sns.heatmap(data_seaborn_diamonds.corr(numeric_only = True), ax = ax1)
    kdeplot_diamonds = sns.kdeplot(data = data_seaborn_diamonds, x = "carat", y = "price", ax = ax2)
    plt.show()

#3.2.5
def my_plot(string_input):
    data_seaborn_diamonds_1 = pd.DataFrame(sns.load_dataset("diamonds"))
    if string_input == "eww":
        #This graph may take some time to load as it is rather busy and complicated
        data_seaborn_diamonds_1["price"] = data_seaborn_diamonds_1["price"].astype('string')
        data_seaborn_diamonds_1.groupby(["price"]).sum().plot(kind = 'pie', y = 'x')
        plt.show()
        #plt.pie(data_seaborn_diamonds_1[1])
        #plt.show()
    elif string_input == "yay":
        sns.regplot(data = data_seaborn_diamonds_1, x = "carat", y = "price")
        plt.title("Graph showing price increase vs. carat")
        plt.show()
    else: 
        print("This function only works when you enter yay or eww")
  
#my_plot("eww")

#3.2.6

#The biggest issue I had was with the function as I did not have any docstring.
#I did not copy the previous version over as it is above this question. The 
#other issues were trailing whitespace multiple times.

def myplot1(string_input):
    
    r""" myplot1(string_input)
    Plotting a good or bad graph depending on the input.

    This function takes a string as an input. If the string is
    equal to "eww", the graph that is returned does not make any sense.
    If the string is equal to "yay", the graph returns a logical and
    easily understandable graph. All other strings lead to a message
    stating that the input should be "eww" or "yay"

    Parameters
    ----------
    string_input : string
                   This is a input string detemining the graph to be displayed
        
    Returns
    -------
    describe : graph or string
               returns either a graph or a string. The graph may be nice or bad, 
               the string will print "This function only works when you enter "yay" 
               or "eww"

    """

    data_seaborn_diamonds_1 = pd.DataFrame(sns.load_dataset("diamonds"))
    if string_input == "eww": 
        #This graph may take some time to load as it is rather busy and complicated
        data_seaborn_diamonds_1["price"] = data_seaborn_diamonds_1["price"].astype('string')
        data_seaborn_diamonds_1.groupby(["price"]).sum().plot(kind = 'pie', y = 'x')
        plt.show()
        #plt.pie(data_seaborn_diamonds_1[1])
        #plt.show()
    elif string_input == "yay":
        sns.regplot(data = data_seaborn_diamonds_1, x = "carat", y = "price")
        plt.title("Graph showing price increase vs. carat")
        plt.show()
    else: 
        print("This function only works when you enter yay or eww")
        
#my_plot("yay")


#3.2.7
#There are many different ways of writing docstring. The most common used way
#is based on reST but I prefer the numpydoc style. For one, I think it looks
#nice and stays readable when the function becomes more complicated. Additionally,
#you can also use this type of docstring and read it in automatically using sphinx/numpydoc


#3.2.8

#Issue 1: All these imports should be placed at the top 
import numpy as np
import numpy.matlib
#This one lead to an error and I could not install it using pip
#import pyjags
import scipy.io as sio
from scipy import stats
import warnings
import os
import matplotlib.pyplot as plt

#Comments were missing. The variable names are fine as they are within the function but 
#could be improved if other functions have similar names. 

def flipstanout(insamples):
    '''
    The docstring is missing for this function so it 
    is not fully clear what it does
    '''
    result = {}  # Initialize dictionary
    allkeys ={} # Initialize dictionary
    keyindx = 0 #Starting point for key index
    #Iterating through each key in the input "insamples"
    for key in insamples.keys():
        #Checks if key is unequal to "_"
        if key[0] != '_':
            #Assigns possamps the value from the dictionary equal to the key
            possamps = insamples[key]
            #Moving the axis
            transamps = np.moveaxis(possamps,0,-1)
            bettersamps = np.moveaxis(transamps,0,-1)
            #Checks if bettersamps is two dimensional 
            if len(bettersamps.shape) == 2:
                #reshapes it
                reshapedsamps = np.reshape(bettersamps, (1,) + bettersamps.shape[0:2])
                #makes the results dictionary for the key equal to the shaped array 
                result[key] = reshapedsamps
            else:
                #makes the results dictionary for the key equal to the shaped array
                result[key] = bettersamps

    #Returns the result once the input has been iterated through 
    return result
