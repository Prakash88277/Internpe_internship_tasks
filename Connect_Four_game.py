import numpy as np

ROW_SIZE = 6
COL_SIZE = 7

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

def Game():
    turn = 0
    while not game_over:
        print_board(board)
        if turn == 0:
            col = int(input("player 1: Enter the valur between (0-6): "))
            if is_valid(board, col):
                drop_val(board, check_row(board, col), col, turn+1)
                if check_for_win(board, turn+1):
                    print_board(board)
                    print("Player 1 is win!!!!!!")
                    break
                turn = 1 - turn
            else:
                print("Not valid...............")
        else:
            col = int(input("player 2: Enter the valur between (0-6): "))
            if is_valid(board, col):
                drop_val(board, check_row(board, col), col, turn+1)
                if check_for_win(board, turn+1):
                    print_board(board)
                    print("Player 2 is win!!!!!!")
                    break
                turn = 1 - turn
            else:
                print("Not valid...............")
        

game_over = False
board = create_board()

if __name__ == "__main__":
    game = Game()
