import random

print("Welcome to Rock, Paper, Scissors!")
answer = input("Rock! Paper! Scissors! Shoot! : ")
num = random.randint(0,2)

if answer == "rock":
    answer = 0
elif answer == "paper":
    answer = 1
else:
    answer = 2

if answer == 1 and num == 0:
    print("computer threw rock\nplayer threw paper \npaper covers rock!  \nPlayer Wins!")
elif answer == 1 and num == 2:
    print("computer threw scissors\nplayer threw paper \nscissors cuts paper!  \nComputer Wins!")
else:
    print("It's a draw!")

print(answer)
print(num)

