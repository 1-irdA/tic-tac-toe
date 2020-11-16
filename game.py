import pygame
from math import floor
from board import Board
from player import Player

ROW = 3
COLUMN = 3
BLACK = (0,0,0)

w = int(400 / 3)
h = int(400 / 3)

game_over = False
turn = 0

def is_valid(row,col):
    return row > -1 and row < 3 and col > - 1 and col < 3

size = (400, 500)

pygame.init()

pygame.display.set_caption('Tic Tac Toe')
icon = pygame.image.load('tic-tac-toe.png')               # load icon         
pygame.display.set_icon(icon)                             # put icon
font = pygame.font.SysFont("comicsansms",30)
screen = pygame.display.set_mode(size)

board = Board()
p_x = Player('X')
p_o = Player('O')

while not game_over:

    screen.fill((255,255,255))
    board.draw_board(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()

        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]

            if turn % 2 == 0:
                coord = (floor(posx / w),floor(posy / w))
                if is_valid(coord[0],coord[1]) and board.is_empty_slot(coord[0],coord[1]):
                    p_x.drop_piece(board.board,coord[0],coord[1])
                    if board.is_winning_move(p_x.piece):
                        label = font.render("PLAYER X WINS !",1,BLACK)
                        screen.blit(label,(75,450))
                        game_over = True
            else:
                coord = (floor(posx / w),floor(posy / w))
                if is_valid(coord[0],coord[1]) and board.is_empty_slot(coord[0],coord[1]):
                    p_o.drop_piece(board.board,coord[0],coord[1])
                    if board.is_winning_move(p_o.piece):
                        label = font.render("PLAYER O WINS !",1,BLACK)
                        screen.blit(label,(75,450))
                        game_over = True

            turn += 1
            board.draw_board(screen)

            if turn == 9 and not game_over:
                label = font.render("TIE !",1,BLACK)
                screen.blit(label,(150,450))
                game_over = True

            pygame.display.update()

            if game_over:
                pygame.time.wait(3000)