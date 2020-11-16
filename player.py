class Player:
    def __init__(self,piece):
        self.piece = piece

    def drop_piece(self,board,row,col):
        board[row][col] = self.piece