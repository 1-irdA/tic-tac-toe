import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
ROW = 3
COLUMN = 3
w = 400 // 3
h = 400 // 3

class Board:
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]

    def is_empty_slot(self, row, col):
        if self.board[row][col] == '':
            return True

    def is_winning_move(self,piece):
        # horizontal 
        for i in range(ROW):
            if self.board[i][0] == piece and self.board[i][1] == piece and self.board[i][2] == piece:
                return True
        # vertical
        for i in range(COLUMN):
            if self.board[0][i] == piece and self.board[1][i] == piece and self.board[2][i] == piece:
                return True

        # diagonal
        if self.board[2][0] == piece and self.board[1][1] == piece and self.board[0][2] == piece:
            return True

        # anti diagonal
        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            return True

    def draw_board(self, surface):
        pygame.draw.line(surface,BLACK,[0,w],[400,w],5)
        pygame.draw.line(surface,BLACK,[0,w*2],[400,w*2],5)
        pygame.draw.line(surface,BLACK,[w,0],[w,400],5)
        pygame.draw.line(surface,BLACK,[w*2,0],[w*2,400],5)
        for i in range(ROW):
            for j in range(COLUMN):
                x = int(w * i + w / 2)
                y = int(w * j + w / 2)
                r = int(w / 4)
                if self.board[i][j] == 'X':
                    pygame.draw.line(surface,BLACK,[x-r,y-r],[x+r,y+r],5)
                    pygame.draw.line(surface,BLACK,[x+r,y-r],[x-r,y+r],5)
                elif self.board[i][j] == 'O':
                    pygame.draw.circle(surface,BLACK,(x,y),40,3)