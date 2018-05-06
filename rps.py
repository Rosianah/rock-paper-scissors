#Rosianah Musyoka

from random import randint
 
options = ["rock", "paper", "scissors"]
 
computer = options[randint(0,2)]
 
#set player to False
player = False
 
name = raw_input("Welcome to this awesome game.\n You will be playing against the computer\n\n Kindly tell me your beautiful name...\n")
while player == False:
#set player to True    
    player = raw_input("Okay " + name + "\n\t ***Kindly do not use any caps*** \n Now make your a choice.\n rock, paper, scissors?\n\n")
    if player == computer:
        print("Computer? "+ computer + "\n" + name + "? " + player + "\n It's a Tie!\n\n")
    elif player == "rock":
        if computer == "paper":
            print("Computer? " + computer+"\n" + name+ "? "+ player +"\n Computer wins!\n\n")
        else:
            print("Computer? " + computer + "\n" + name + "? "  + player  + "\n Hurray!! You win\n\n")
    elif player == "paper":
        if computer == "scissors":
            print("Computer? " + computer + "\n" + name + "? " + player  + "\n Computer wins!\n\n")
        else:
            print("Computer? "  + computer + "\n" + name + "? " + player  + "\n Hurray!! You win\n\n")
    elif player == "scissors":
        if computer == "rock":
            print("Computer? "  + computer +"\n"  + name + "? "  + player  + "\n Computer wins!\n\n")
        else:
            print("Computer? "  + computer + "\n"  + name + "? "  +player  + "\n Hurray!! You win\n\n")
    else:
        print("This is not a valid object selection!!")
    
    player = False
    computer = options[randint(0,2)]
