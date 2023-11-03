def main():
    RANGEMAX=1000
    RANGEMIN=1
    choice=1
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
    number=ranged_random_int()
    guess_game(number,player1, player2)
def guess_game(number,player1,player2):
    roundnumber=1
    while answer1!=number, or answer2!=number:
        print("Round", roundnumber)
        answer1=input(float("What is the random number", player1,"?"))
        answer1=round(answer1)
        answer2=input(float("What is the random number", player2,"?"))
        answer1=round(answer1)
        roundnumber+=1
    if answer1==number:
        print("YOU WIN", player1)
    elif answer2==number:
        print("YOU WIN", player2)

            