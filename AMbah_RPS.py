import random

# ASCII art Sourced from gitHub user wyand1004
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'    ____)____
            ______)
           _______)
          _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


# printMove function
# return an ascii pattern of the move
def printMove(move):
    if move == 'rock':
        return rock
    if move == 'paper':
        return paper
    if move == 'scissors':
        return scissors


# makePlayerMove function    
def makePlayerMove(playerName):
    playerMove = input("Choose rock, paper or scissors:").lower()
    playerArt = printMove(playerMove)
    print()
    print(playerName + " choose:")
    print(playerArt)
    return playerMove


# makeComputerMove function
def makeComputerMove(computerName):
    random_num = random.randint(1, 3)
    computerMove = ""
    if random_num == 1:
        computerMove = 'rock'
    elif random_num == 2:
        computerMove = 'paper'
    else:
        computerMove = 'scissors'
    computerArt = printMove(computerMove)
    print()
    print(computerName + " choose:")
    print(computerArt)
    return computerMove


# checkRoundWinner
def checkRoundWinner(playerMove, computerMove):
    if playerMove == computerMove:
        return "Tie"
    if playerMove == 'rock' and computerMove == 'scissors':
        return "Player Won"
    elif playerMove == 'paper' and computerMove == 'rock':
        return "Player Won"
    elif playerMove == 'scissors' and computerMove == 'paper':
        return "Player Won"
    return "Computer Won"


def main():
    playerName = input("Enter player name: ")
    computerName = input("Enter computer name: ")
    playerWon = 0
    computerWon = 0
    roundNo = 1
    while playerWon < 2 and computerWon < 2:
        print()
        print("ROUND {}".format(roundNo))
        print()
        playerMove = makePlayerMove(playerName)
        computerMove = makeComputerMove(computerName)
        result = checkRoundWinner(playerMove, computerMove)
        if result == "Player Won":
            playerWon += 1
            print(playerName + " won the round!")
        elif result == "Computer Won":
            computerWon += 1
            print(computerName + " won the round!")
        else:
            print("It was a tie!")
        roundNo += 1

    if playerWon == 2:
        print(playerName + " won the match!")
    elif computerWon == 2:
        print(computerName + " won the match!")


main()
