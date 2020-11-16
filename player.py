"""
Class who represent the player
"""
class Player:

    """
    Init player token
    -   piece (X or O)
    """
    def __init__(self, piece):
        self.piece = piece

    """
    Player put token on board 
    at row col position
    -   board tictactoe board
    -   row position
    -   col position
    """
    def drop_piece(self,board,row,col):
        board[row][col] = self.piece