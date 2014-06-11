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
        return self.board == other.board
