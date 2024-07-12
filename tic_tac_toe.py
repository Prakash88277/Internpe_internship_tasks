def board(Xspace, Ospace):
    Update = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for value in range(0, 9):
        i = int(value/3)
        j = int(value%3)
        Update[i][j] = 'X' if Xspace[i][j] else 'O' if Ospace[i][j] else value
    print("-----------")
    print(f" {Update[0][0]} | {Update[0][1]} | {Update[0][2]}")
    print("___|___|___")
    print(f" {Update[1][0]} | {Update[1][1]} | {Update[1][2]}")
    print("___|___|___")
    print(f" {Update[2][0]} | {Update[2][1]} | {Update[2][2]}")
    print("-----------")

def win(Xspace, Ospace):
    if sum(Xspace):
        print("The winner is X")
        return 1
    if sum(Ospace):
        print("The winner is O")
        return 0
    return -1

def sum(space):
    return 1 if space[0][0] + space[0][1] + space[0][2] == 3 or space[1][0] + space[1][1] + space[1][2] == 3 or space[2][0] + space[2][1] + space[2][2] == 3 or space[0][0] + space[1][0] + space[2][0] == 3 or space[0][1] + space[1][1] + space[2][1] == 3 or space[0][2] + space[1][2] + space[2][2] == 3 or space[0][0] + space[1][1] + space[2][2] == 3 or space[0][2] + space[1][1] + space[2][0] == 3 else 0
        

Xspace = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

Ospace = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
loop = True
turn = 1 # 1 is for X and 0 is for O
print("Your game is start: ")
while loop:
    print("it is X's turn: ") if turn else print("it is O's turn: ")
    board(Xspace, Ospace)
    val = int(input("Enter the value b/w 0-8: "))
    i = int(val/3)
    j = int(val%3)
    if turn == 0:
        Ospace[i][j] = 1 if not Ospace[i][j] and Xspace[i][j] == 0 else print(f"{val} is already occupied")
        turn = 1
    else:
        Xspace[i][j] = 1 if Ospace[i][j] == 0 and Xspace[i][j] == 0 else print(f"{val} is already occupied")
        turn = 0
    if win(Xspace, Ospace) != -1:
        break