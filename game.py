board = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

def show_board(f):
    print(" 0 1 2")
    for i in range(len(board)):
        print(i, *board[i])


def player_step(f, user):
    print(f'Куда поставим {user}?')
    while True:
        x = int(input('Введите номер строки:'))
        y = int(input('Введите номер столбца:'))
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

def check_win(f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False

def game(f):
    show_board(board)
    count = 0
    while True:
        if count%2 == 0:
            user = 'X'
        else: user = '0'
        if count == 9:
            print('Ничья')
            break
        if count < 9:
            x, y = player_step(board, user)
            board[x][y] = user
        if check_win(board, user):
            print(f'Выиграл {user}')
            break
        show_board(board)
        count += 1
game(board)








