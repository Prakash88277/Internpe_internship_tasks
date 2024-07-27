import numpy as np
import pygame
import sys

ROW_SIZE = 6
COL_SIZE = 7

RED = (255, 165, 0)
YELLOW = (30, 144, 255)

pygame.init()
pygame.display.set_caption('Connect Four Game')

BLOCK_SIZE = 100
width = COL_SIZE * BLOCK_SIZE
heigth = (ROW_SIZE+1) * BLOCK_SIZE

display = pygame.display.set_mode((width, heigth))

def create_board():
    board = np.zeros((ROW_SIZE, COL_SIZE))
    return board

def is_valid(board, col):
    return board[ROW_SIZE-1][col] == 0

def check_row(board, col):
    for r in range(ROW_SIZE):
        if board[r][col] == 0:
            return r

def drop_val(board, row, col, player):
    board[row][col] = player

def check_for_win(board, player):
    for c in range(COL_SIZE-3):
        for r in range(ROW_SIZE):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True
            
    for c in range(COL_SIZE):
        for r in range(ROW_SIZE-3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
            
    for c in range(COL_SIZE-3):
        for r in range(ROW_SIZE-3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
            
    for c in range(COL_SIZE-3):
        for r in range(3, ROW_SIZE):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
    return False

def print_board(board):
    print(np.flip(board, 0))

def drow_board():
    for c in range(COL_SIZE):
        for r in range(ROW_SIZE):
            pygame.draw.rect(display, (211, 211, 211), (c*BLOCK_SIZE, r*BLOCK_SIZE+BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.circle(display, (194, 118, 118), (c*BLOCK_SIZE+BLOCK_SIZE/2, (r*BLOCK_SIZE+BLOCK_SIZE/2)+BLOCK_SIZE), int((BLOCK_SIZE/2)-5))

    for c in range(COL_SIZE):
        for r in range(ROW_SIZE):
            if board[r][c] == 1:
                pygame.draw.circle(display, RED,(c*BLOCK_SIZE+BLOCK_SIZE/2, heigth - int(r*BLOCK_SIZE+BLOCK_SIZE/2)), int((BLOCK_SIZE/2)-5))
            elif board[r][c] == 2:
                pygame.draw.circle(display, YELLOW, (c*BLOCK_SIZE+BLOCK_SIZE/2, heigth - int(r*BLOCK_SIZE+BLOCK_SIZE/2)), int((BLOCK_SIZE/2)-5))

    pygame.display.flip()

def Game():
    game_over = False
    turn = 0
    font = pygame.font.SysFont("monospace", 45, False, True)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(display, (232, 144, 144), (0, 0, width, BLOCK_SIZE))
                if turn == 0:
                    pygame.draw.circle(display, RED, (event.pos[0], BLOCK_SIZE//2), (BLOCK_SIZE//2)-5)
                if turn == 1:
                    pygame.draw.circle(display, YELLOW, (event.pos[0], BLOCK_SIZE//2), (BLOCK_SIZE//2)-5)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    col = int(event.pos[0]/100) % COL_SIZE
                    if is_valid(board, col):
                        drop_val(board, check_row(board, col), col, turn+1)
                        if check_for_win(board, turn+1):
                            print_board(board)
                            pygame.draw.rect(display, (0, 0, 0), (0, 0, width, BLOCK_SIZE))
                            display.blit(font.render("!!! Player 1 is WIN !!!", 1, RED), (40, 25))
                            game_over = True
                        turn = 1 - turn
                    else:
                        print("Not valid...............")
                else:
                    col = int(event.pos[0]/100) % COL_SIZE
                    if is_valid(board, col):
                        drop_val(board, check_row(board, col), col, turn+1)
                        if check_for_win(board, turn+1):
                            print_board(board)
                            pygame.draw.rect(display, (0, 0, 0), (0, 0, width, BLOCK_SIZE))
                            display.blit(font.render("!!! Player 2 is WIN !!!", 1, YELLOW), (40, 25))
                            game_over = True
                        turn = 1 - turn
                    else:
                        print("Not valid...............")
                print_board(board)
                print(event.pos)
        drow_board()
        


board = create_board()

if __name__ == "__main__":
    game = Game()
    pygame.time.wait(3000)
