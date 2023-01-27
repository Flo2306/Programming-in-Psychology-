#Poker Game 
import matplotlib.pyplot as plt
import random
from collections import Counter 
def poker_simulation(): 
    #Setting up the deck. I am using 11,12,13,14 to represent jack,queen,king, and ace as it makes interacting easier. 
    Suits = ["Heart", "Spades", "Clubs", "Diamonds"]
    Numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    deck = list()
    #Combining all potential values into strings and adding them to a list
    for suit in Suits:
        for number in Numbers: 
            deck.append(number + " of " + suit)

    #Drawing random cards 
    cards_drawn = random.sample(deck, 5)
    numbers_drawn = []
    suits_drawn = []

    #Creating a list of suits drawn and numbers drawn 
    for card in cards_drawn:
        numbers_drawn.append(int(card.split()[0]))
        suits_drawn.append(card.split()[2])

    #Setting up a variable indicating a win or a loss 
    win = 0 

    #For three of same kind 
    #Counter is a function that counts how often values/strings appear within a list 
    counts_of_numbers = Counter(numbers_drawn)
    similarities_number = counts_of_numbers.values()

    #Check if any card appeared at least three times
    outcome_three = any(ele >= 3 for ele in similarities_number)
    if outcome_three == True:
        win = 1


    #For Straight 
    #Creating a binary outcome indicating whether the numbers drawn are similar to a list with range of 
    #min value to max value 
    outcome_straight = numbers_drawn.sort() == list(range(min(numbers_drawn), max(numbers_drawn)))
    if outcome_straight == True:
        win = 1

    #For Flush 
    #Similar approach to three of one kind
    counts_of_suits = Counter(suits_drawn)
    similarities_suit = counts_of_suits.values()

    outcome_flush = any(ele == 5 for ele in similarities_suit)

    if outcome_flush == True:
        win = 1

    #For Full House 
    #Simple hard coding of possibilities related to a full hourse as it 
    #can take only two ways 
    if similarities_number == [3,2] or similarities_number == [2,3]:
        win = 1

    #For Straight Flush 
    #This one is theoretically unnecessary as money will be awarded if there is a straight anyways 
    if outcome_straight == True and outcome_flush == True:
        win = 1

    return win 

def run_poker():
    #Setting up a list of money 
    list_of_money = []
    #Starting Money 
    starting_money = 200
    #For a more interesting results, play around with the values and see the outcome. 
    #Point of improvement: Make a further simulation to find values for money won and lost 
    #that leads to a stable outcome of money on average 
    #Money lost each round 
    money_lost = 1
    #Money won each round 
    money_won = 30 
    #Creating a while loop 
    while 1 == True:
        #Appending current money value to list of money 
        list_of_money.append(starting_money)
        #When the money becomes 0, the loop breaks 
        if starting_money == 0:
            print("Go home, you lost all your money")
            break
        #Asking the person if they want to go home once the value is above 300 Euros. 
        #Point of Improvement: Only present question once each time value is above 300 Euros but 
        #I lacked the time to implement this
        if starting_money >= 300: 
            print(f"You have {starting_money} Euros, you should go home")
            go_home = input("Do you want to go home? Enter y/n: ")
            if go_home == "y":
                print("Wise decision")
                break
            else: 
                print("Your call")
        #Calling the function and adding or taking away money depending on the outcome
        if poker_simulation() == 1:
            starting_money = starting_money + money_won
        else: 
            starting_money = starting_money - money_lost


    #Plotting the list_of_money 
    plt.plot(list(range(len(list_of_money))), list_of_money)
    plt.title("Money won over multiple games of Poker")
    plt.xlabel("Games")
    plt.ylabel("Money")
    plt.show()
