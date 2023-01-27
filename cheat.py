import videopoker_copy as poker
import sequences_copy as seq 
import Assignment_32_copy as assignment 

#Order of calling function: 
#1 = poker simulation 
#2 = printing all prime numbers below value
#3 = plotting a random graph 
#4 = plotting a graph about diamonds 
#5 = plotting a graph about tips and bill 
#6 = plotting a graph about people surviving the titanic 
#7 = plotting random numbers 
#Everything above leads to a message being printed 

def cheat(assignment_number): 
    '''
    I have written too much docstring today 
    but just for you to see that I have it here 
    '''
    if assignment_number == 1:
        poker.run_poker()
    elif assignment_number == 2: 
        seq.prime(15)
    elif assignment_number == 3: 
        assignment.my_plot("eww")
    elif assignment_number == 4:
        assignment.plot_diamonds()
    elif assignment_number == 5:
        assignment.plot_money()
    elif assignment_number == 6: 
        assignment.plot_titanic
    elif assignment_number == 7:
        assignment.plot_random()
    else: 
        print("The number you have specified does not lead to a function being called")


cheat(1)
