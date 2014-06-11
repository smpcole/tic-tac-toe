from Board import *
from Player import *

def main():
    board = Board()
    players = (HumanPlayer('x', board), HumanPlayer('o', board))
    turnNum = 0
    currentPlayer = None
    while not board.endGame():
        currentPlayer = players[turnNum % 2]
        print "%s's turn" % currentPlayer
        currentPlayer.takeTurn()
        print board
        turnNum += 1
    if board.winner != None:
        print "%ss win!" % board.winner
    else:
        print "It's a tie!"

if __name__ == "__main__":
    main()
