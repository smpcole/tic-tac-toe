class Player:

    def __init__(self, symbol, board):
        self.symbol = symbol
        board.players[symbol] = self
        self.board = board

    def __str__(self):
        return self.symbol

class ComputerPlayer(Player):

    def __init__(self, symbol, board):
        Player.__init__(self, symbol, board)
        self.outcomes = {}

    def takeTurn(self):
        bestMove = None
        bestOutcome = "lose"

        # Try moving to all possible spaces
        for i in xrange(3):
            for j in xrange(3):
                if self.board[i][j] == ' ':
                    self.board.write(self.symbol, i, j)
                    outcome = self.outcome(self.board, self.board.otherSymbol(self.symbol))

                    # If this outcome is an improvement over the previous best
                    if bestOutcome == "lose" or (bestOutcome == "draw" and outcome == "win"):
                        bestMove = (i, j)
                        bestOutcome = outcome
                    
                    self.board.write(' ', i, j)

                    # Can stop immediately as soon as you win
                    if bestOutcome == "win":
                        break
            if bestOutcome == "win":
                break
        self.board.write(self.symbol, bestMove[0], bestMove[1])

    def outcome(self, board, currentSymbol):
        """Determine whether player wins, loses, or draws on board via dynamic programming.  Player wins if he can force a win, draws if he can force a draw, loses otherwise"""

        # Check whether this board has already been solved        
        if board not in self.outcomes or currentSymbol not in self.outcomes[board]:
            outcome = None
            # Base cases
            if board.endGame():
                if board.winner == self:
                    outcome = "win"
                elif board.winner == None:
                    outcome = "draw"
                else:
                    outcome = "lose"

            else:

                # Store outcomes in increasing order of how good they are for the current player
                outcomes = ["lose", "draw", "win"]
                if self.symbol != currentSymbol:
                    outcomes.reverse()

                outcome = outcomes[0]

                # Try moving to every open space
                for i in xrange(3):
                    for j in xrange(3):
                        if board[i][j] == ' ':
                            board.write(currentSymbol, i, j)
                            newOutcome = self.outcome(board, self.board.otherSymbol(currentSymbol))

                            # Current player wins iff. he can move to a winning configuration
                            # Current player loses iff. all moves lead to losing configurations

                            # Update outcome if newOutcome is an improvement
                            if newOutcome == outcomes[2] or (newOutcome == outcomes[1] and outcome == outcomes[0]):
                                outcome = newOutcome
                            
                            board.write(' ', i, j)

                            # Can stop as soon as you win
                            if outcome == outcomes[2]:
                                break

                    if outcome == outcomes[2]:
                        break

            if board not in self.outcomes:
                self.outcomes[board] = {}
            self.outcomes[board][currentSymbol] = outcome

        return self.outcomes[board][currentSymbol] 

class HumanPlayer(Player):

    def takeTurn(self):
        board = self.board
        isValid = False
        while(not isValid):
            move = raw_input("Where would you like to move?\nEnter coordinates: ").strip().split()
            for i in xrange(2):
                move[i] = int(move[i])
            if board[move[0]][move[1]] == ' ':
                isValid = True
                board.write(self.symbol, move[0], move[1])
            else:
                print "Sorry, %d %d is already occupied." % (move[0], move[1])
