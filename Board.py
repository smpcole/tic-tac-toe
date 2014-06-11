class Board:
    
    def __init__(self):
        self.board = [[" " for j in xrange(3)] for i in xrange(3)]

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
                if self[i][j] == 'x':
                    digit = 1
                elif self[i][j] == 'o':
                    digit = 2
                h = 3 * h + digit
        return h
                
