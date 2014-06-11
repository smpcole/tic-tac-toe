class Player:
    players = {} # Store pointers to 'x' player and 'o' player
    def __init__(self, symbol):
        self.symbol = symbol
        Player.players[symbol] = self

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
                board.spacesLeft -= 1
            else:
                print "Sorry, %d %d is already occupied." % (move[0], move[1])
