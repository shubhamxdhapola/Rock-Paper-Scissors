import random

# Function to decide result of game
def rock_paper_scissors(playerMove, computerMove,result):

    if playerMove == 1: playerMove = "Rock"
    elif playerMove == 2: playerMove = "Paper"
    else: playerMove = "Scissors"

    if computerMove == 1: computerMove = "Rock"
    elif computerMove == 2: computerMove = "Paper"
    else: computerMove = "Scissors"
         
    print(f">> Your Move : {playerMove} ")
    print(f">> Computer's Move : {computerMove} ")
    print(f">> Result : {result}")


# Function to calculate final result
def finalResult(roundsCounter, playerWin, computerWin, drawRounds):
    
    print("")
    print("--------------------------------")
    print(f">> Final Result <<")
    print("--------------------------------")

    print(f">> Total Rounds : {roundsCounter-1} ")
    print(f">> You Won : {playerWin}")
    print(f">> Computer Won : {computerWin} ")
    print(f">> Draw : {drawRounds}")
   
    if playerWin > computerWin : winner = "You"
    elif computerWin > playerWin : winner = "Computer"
    else: winner = "Draw"
    print(f">> Final Winner : {winner}")   


# Greeting user
print("\n-------------WELCOME TO ROCK, PAPER AND SCISSORS-------------\n")
print(">> PRESS 1 FOR ROCK \n>> PRESS 2 FOR PAPER \n>> PRESS 3 FOR SCISSORS")


try:
    rounds = int(input("\n>> How many rounds you want to play? : ")) #Total rounds user want to play
    roundsCounter = 1 # Count the total number of rounds
    playerWin = 0 # Stores total rounds won by player
    computerWin = 0 # Stores total rounds won by computer
    drawRounds = 0 # Stores total draw rounds
    
    while (rounds > 0):
    
        computer_move = random.randint(1,3) # Generating computer move
    
        print("\n--------------------------------")
        print(f">> Round : {roundsCounter} <<") # Display current round
        print("--------------------------------")
       
        player_move = int(input(">> Enter your move : ")) # Taking user move as input
    
        if (player_move < 4) and (player_move > 0):
            
            #This block will execute only if the user wins
            if (player_move == 1 and computer_move == 3) or (player_move == 3 and computer_move == 2) or (player_move == 2 and computer_move == 1):
            
                result = "You Won!!"
                rock_paper_scissors(player_move, computer_move, result) # Caling the 'rock_paper_scissors' function
                playerWin +=1 # increase the value of 'playerWin' by 1
            
            #This block will if there is a draw
            elif player_move == computer_move:
            
                result = "Draw"
                rock_paper_scissors(player_move, computer_move, result)
                drawRounds +=1  # increase the value of 'drawRounds' by 1
    
            #This block will execute if computer wins
            else: 
            
                result = "You Lose!!"
                rock_paper_scissors(player_move, computer_move, result)
                computerWin+=1  # increase the value of 'computerWin' by 1
        
        # This block will execute if user enters a value greater than 4 and less than 1
        else:
            print(">> Invalid input! Please enter between 1 to 3")
        
        rounds-=1 # Decrement the value of 'rounds' by 1 after completion of one round
        roundsCounter+=1 # Increment the value of 'roundsCounter' by 1 to track ongoing round

    finalResult(roundsCounter, playerWin, computerWin, drawRounds) # Calling 'finalResult' function which calculate final result
    print("")

except ValueError:
    print("Invalid input! Please enter a valid input")

