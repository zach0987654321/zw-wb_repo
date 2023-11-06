def main():
    RANGEMAX=1000
    RANGEMIN=1
    choice=0
    while choice!=1:
        choice=menu()
        if choice==2:
            ranged=choose_range()
            RANGEMAX=ranged[1]
            RANGEMIN=ranged[0]
        elif choice==1:
            player=player_name()
            player1=player[0]
            player2=player[1]
        elif choice==3:
            exit
        else:
            print("YOU DID NOT TYPE A VALID NUMBER")
            main()
    generated_number=ranged_random_int(RANGEMIN,RANGEMAX)
    guess_game(generated_number,player1, player2)
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
    while choice <= 0.9 or choice >= 3.1:
        choice = int(input('Enter a number between 1 and 3: '))
    
    return choice

def player_name():
#Get input for name
#Return name
    
    name1 = input("Enter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    
    return name1, name2


def choose_range():
    #lets player choose range of the random number
    min_num = int(input('What do you want the minumum number to be? '))
    max_num = int(input('What do you want the maximum number to be? '))
    while min_num >= max_num:
        print('Make sure the minumum number is less than the maximum!!!')
        min_num = int(input('What do you want the minumum number to be? '))
        max_num = int(input('What do you want the maximum number to be? '))
        
    return min_num, max_num
    
    

def ranged_random_int(min_num, max_num):
    import random
#Return min_num and max_num
#Returns minimum and maximum value
    generated_number=random.randint(min_num, max_num)
    
    return generated_number
    
def guess_game(number,player1,player2):
    roundnumber=1
    answer1=-100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    answer2=-100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    while answer1!=number or answer2!=number:
        print("Round", roundnumber)
        print(number)
        print("What is the random number", player1,"?")
        answer1=float(input())
        answer1=round(answer1)
        print("What is the random number", player2,"?")
        answer2=float(input())
        answer2=round(answer1)
        roundnumber+=1
    if answer1==number:
        print("YOU WIN", player1)
    elif answer2==number:
        print("YOU WIN", player2)

            