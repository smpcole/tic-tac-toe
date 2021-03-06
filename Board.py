class Board:
    
    def __init__(self, stringRep = "         "):
        self.board = [[" " for j in xrange(3)] for i in xrange(3)]
        self.winner = None
        self.spacesLeft = 9
        for i in xrange(3):
            for j in xrange(3):
                self.write(stringRep[3 * i + j], i, j)
        self.players = {} # Store pointers to 'x' player and 'o' player

    def otherSymbol(self, symbol):
        """Return first symbol that is different from given symbol"""
        for otherSymbol in self.players:
            if symbol != otherSymbol:
                return otherSymbol

    def write(self, symbol, i, j):
        old = self[i][j]
        self[i][j] = symbol
        if symbol != ' ' and old == ' ':
            self.spacesLeft -= 1
        elif symbol == ' ' and old != ' ':
            self.spacesLeft += 1

    def copy(self):
        cpy = Board();
        for i in xrange(3):
            for j in xrange(3):
                cpy[i][j] = self[i][j]
        cpy.players = self.players
        cpy.spacesLeft = self.spacesLeft
        cpy.winner = self.winner
        return cpy

    def __getitem__(self, i):
        return self.board[i]

    def __str__(self):
        str = ""
        for i in xrange(3):
            for j in xrange(3):
                str += self.board[i][j]
            str += "\n"
        return str

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        """Return a number between 0 and 3^9 - 1.  Two boards have same hash iff. they are the same"""
        h = 0
        for i in xrange(3):
            for j in xrange(3):
                digit = 0
                if self[i][j] == self.players.keys()[0]:
                    digit = 1
                elif self[i][j] == self.players.keys()[1]:
                    digit = 2
                h = 3 * h + digit
        assert 0 <= h and h < 3 ** 9
        return h
                
    def endGame(self):
        """Check for 3 in a row"""
        for i in xrange(3):
            # Rows
            if self[i][0] == self[i][1] and self[i][1] == self[i][2] and self[i][0] != ' ':
                self.winner = self.players[self[i][0]]
                return True
            # Columns
            if self[0][i] == self[1][i] and self[1][i] == self[2][i] and self[0][i] != ' ':
                self.winner = self.players[self[0][i]]
                return True

        # Diagonals
        if self[0][0] == self[1][1] and self[1][1] == self[2][2] and self[0][0] != ' ':
            self.winner = self.players[self[0][0]]
            return True
        if self[0][2] == self[1][1] and self[1][1] == self[2][0] and self[0][2] != ' ':
            self.winner = self.players[self[0][2]]
            return True

        # Check for tie
        if self.spacesLeft == 0:
            self.winner = None
            return True

        return False
