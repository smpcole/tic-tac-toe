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
                    outcome = self.outcome(self.board)

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

    def outcome(self, board):
        """Determine whether player wins, loses, or draws on board via dynamic programming.  Player wins if he can force a win, draws if he can force a draw, loses otherwise"""

        # Check whether this board has already been solved        
        if board not in self.outcomes:
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
                outcome = "lose"
                nextMove = board.copy()

                # Try moving to every open space
                for i in xrange(3):
                    for j in xrange(3):
                        if nextMove[i][j] == ' ':
                            nextMove.write(self.symbol, i, j)
                            newOutcome = self.outcome(nextMove)
                            if newOutcome == "win":
                                outcome = "win"
                            elif outcome == "lose": # Only change outcome if currently losing
                                outcome = newOutcome
                            nextMove.write(' ', i, j)

                            # Stop if you win
                            if outcome == "win":
                                break

                    if outcome == "win":
                        break

            self.outcomes[board] = outcome

        return self.outcomes[board] 

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
