class Player:

    def __init__(self, symbol):
        self.symbol = symbol

class HumanPlayer(Player):

    def takeTurn(self, board):
        isValid = False
        while(not isValid):
            move = raw_input("Where would you like to move?\nEnter coordinates: ").strip().split()
            for i in xrange(2):
                move[i] = int(move[i])
            if board[move[0]][move[1]] == ' ':
                isValid = True
                board[move[0]][move[1]] = self.symbol
            else:
                print "Sorry, %d %d is already occupied." % (move[0], move[1])
