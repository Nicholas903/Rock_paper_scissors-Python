import random

plays = ["ROCK","PAPER","SCISSORS"]
humanWins = [-2, 1]
humanCount = 0
computerCount = 0
humanChoice = False
playContinue = True


def getValidHumanPlay( low, high ):

        while humanChoice == False:
                
                humanInput = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors"))
	
                if humanInput >= low and humanInput <= high:
                        humanChoice = True
                else:
                        humanChoice = False
	return

def getPlay( human, plays ):
        
        while playContinue == True:
                humanPlay = getValidHumanPlay(0,2)
                computerPlay = random.randint(0,2)
                print("Human chose ",humanPlay)
                print("Computer chose ",computerPlay)
                if humanPlay == computerPlay:
                        PlayContinue = True
                else:
                        playContinue = False
        
	return 

def checkWinner( play, plays, humanCount, computerCount ):
        result = play[0]-play[1]
        if result in humanWins:
                humanCount += 1
                print("Human won with",plays(humanPlay),"beating",plays(computerPlay)
        else:
                computerCount += 1
                print("Computer won with",plays(computerPlay),"beating",plays(humanPlay)

	return 


### Beginning of Main

human = input( "Enter your name ").upper()

keepPlaying = True

while keepPlaying:
	#create a variable called play and call the getPlay function, sending human and plays variable
	#using humanCount and computerCount, call the checkWinner function and send the variables: play, plays, humanCount, computerCount as parameters
	#using the keepPlaying variable do a conditional statement check that computerCount is less than 3 and humanCount is less than 3

#create an if-statement (not inside the while loop) that checks if the human has won 3 times
	#if the human has won 3 times declare that they have won the match and display humanCount to computerCount
#else if the computer has won, declare they have won the match and display computerCount to humanCount
