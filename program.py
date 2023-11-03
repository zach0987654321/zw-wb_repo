def main():
    RANGEMAX=1000
    RANGEMIN=1
    print(player1, player2)
    choice=1
    while choice!=3:
        choice=menu()
        if choice==2:
            RANGEMAX=ranged_randomint()
            RANGEMIN=ranged_randomint()
        elif choice==1:
            player=player_name()
            player1=player[0]
            player2=player[1]
        elif choice==3:
            exit
            