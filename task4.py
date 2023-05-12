
# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

# Создаем пустое поле
board = [" " for i in range(9)]

# Функция для отображения поля на экране
def print_board():
    row1 = "|".join(board[0:3])
    row2 = "|".join(board[3:6])
    row3 = "|".join(board[6:9])
    print(row1)
    print("-" * 5)
    print(row2)
    print("-" * 5)
    print(row3)

# Функция для проверки победителя
def check_winner(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Игровой цикл
current_player = "X"
while True:
    print_board()
    print("Ход игрока", current_player)
    move = input("Выберите ячейку (1-9): ")
    if board[int(move) - 1] == " ":
        board[int(move) - 1] = current_player
        if check_winner(current_player):
            print_board()
            print("Игрок", current_player, "победил!")
            break
        if " " not in board:
            print_board()
            print("Ничья!")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("Ячейка занята. Выберите другую.")