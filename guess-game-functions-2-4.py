import random

def menu():
    import time
#Return choice
    print('Welcome to the guessing game!')
    time.sleep(1.5)
    print('')
    
    print('1.\tStart New Game')
    print('2.\tChoose Range')
    print('3.\tExit')
    
    choice = int(input(''))
    while choice =< 0.9 or => 3.1:
        choice = int(input('Enter a number between 1 and 3: '))
    
    return choice
    pass #???
    
    
def player_name():
#Get input for name
#Return name
    
    name1 = input("Enter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    
    return name1, name2
    pass #???


def choose_range():
    #lets player choose range of the random number
    min_num = int(input('What do you want the minumum number to be? '))
    max_num = int(input('What do you want the maximum number to be? '))
    while min_num >= max_num:
        print('Make sure the minumum number is less than the maximum!!!')
        min_num = int(input('What do you want the minumum number to be? '))
        max_num = int(input('What do you want the maximum number to be? '))
        
    return min_num, max_num
    pass
    

def ranged_random_int():
#Return min_num and max_num
#Returns minimum and maximum value
    generated_number= = random.randint(min_num, max_num)
    
    return generated_number
    pass #???
    