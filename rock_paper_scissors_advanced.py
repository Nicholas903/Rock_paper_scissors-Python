import random

plays = ["ROCK","PAPER","SCISSORS"]
humanWins = [-2, 1]
humanCount = 0
computerCount = 0


def getValidHumanPlay( low, high ):
        humanChoice = False

        while humanChoice == False:

                humanInput = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

                if humanInput <= high and humanInput >= low:
                        humanChoice = True
                else:
                        humanChoice = False
                        
        return humanInput

def getPlay( human, plays ):
        playContinue = True
        while playContinue == True:
                humanPlay = getValidHumanPlay(0,2)
                computerPlay = random.randint(0,2)

                print(human,"chose ",plays[humanPlay])
                print("Computer chose ",plays[computerPlay])
                if humanPlay == computerPlay:
                        playContinue = False
                        break
                break
        return humanPlay,computerPlay


def checkWinner( play, plays, humanCount, computerCount ):
        result = play[0] - play[1]
        if result in humanWins:
                humanCount += 1
                print(human,"won with",plays[play[0]],"beating",plays[play[1]])
        
        elif play[0] == play[1]:
                print ("It is a tie")
                
        else:
                computerCount += 1
                print("Computer won with",plays[play[1]],"beating",plays[play[0]])

        return humanCount, computerCount



human = input( "Enter your name ").upper()

keepPlaying = True

while keepPlaying:
        play = getPlay(human, plays)
        scoreList = checkWinner( play, plays, humanCount, computerCount )
        humanCount = scoreList[0]
        computerCount = scoreList[1]

        if computerCount < 3 and humanCount < 3:
                keepPlaying = True
        else:
                keepPlaying = False
if humanCount == 3:
        print(human,"has won the match",humanCount,"-",computerCount)
else:
                
        print("Computer has won the match",computerCount,"-",humanCount)


