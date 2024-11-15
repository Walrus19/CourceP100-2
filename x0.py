import os
import random
import copy


PLAYERS = {2: 'o',1: 'x'}
# current_player = 1
#
# field = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
# field_comp = [(0,0),(0,1),(0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
# for row in field:
#     for cell in row:
#         print(cell, end=" ")
#     print()

def is_win(field):
    # Работаю с полем только 3x3
    size = len(field)  ## 3
    # Проход по строке
    if field != [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]:
        for row in field:
            if row[0] == row[1] == row[2] and row[0] and row[0] != "[ ]" and row[1] != "[ ]" and row[2] != "[ ]":
                    return True
            # Проход по столбцу
        for i in range(size):
            if field[0][i] == field[1][i] == field[2][i] and field[0][i] and field[0][i] != "[ ]":
                return True

        # Главаная диагональ
        if field[0][0] == field[1][1] == field[2][2] and field[0][0] and field[0][0] != "[ ]" and field[1][1] != "[ ]" and field[2][2] != "[ ]":
            return True
        # Побочная диагональ
        if field[0][2] == field[1][1] == field[2][0] and field[0][2] and field[0][2] != "[ ]" and field[1][1] != "[ ]" and field[2][0] != "[ ]":
            return True

    return False


def move(current_player, label, field, field_c, verbose=True):
        # os.system('cls||clear')
        if current_player == 'c':
            position = random.choice(field_c)
            field_c.remove(position)
            field[position[0]][position[1]] = ' ' + label + ' '
            print()
        else:
            position = input(f'Введите позицию игрок ({label}):').split(sep=',')
            if field[int(position[0])][int(position[1])] == '[ ]':
                field[int(position[0])][int(position[1])] = ' ' + label + ' '
                field_c.remove((int(position[0]), int(position[1])))
            else:
                print('Ошибочный ввод')
                move(current_player, label, field, field_c, verbose=verbose)
        if verbose:
            for row in field:
                for cell in row:
                    print(cell, end=" ")
                print()



def game(verbose=True, players = ['c', 'c'], labels=['x', 'o']):
    cur_index = 0
    current_player = players[cur_index]
    label = labels[cur_index]
    field = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]
    field_comp = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    if verbose:
        for row in field:
            for cell in row:
                print(cell, end=" ")
            print()

    for i in range(9):
        move(current_player, label, field, field_comp, verbose=verbose)
        if is_win(field):
            if verbose:
                print(f'Вы выиграли!, player = {label}')
            return (label, )
        cur_index = 1 if cur_index == 0 else 0
        current_player, label = players[cur_index], labels[cur_index]
    if i == 8:
        if verbose:
            print("Ничья")
    return (0, )



def init(count, verbose=True, players = ['c', 'c'], labels=['x', 'o']):
    stats = {0: 0, 'x' : 0, 'o' : 0}
    for _ in range(count):
        if verbose:
            print('\n\n')
            print('Новая игра')
        result = game(verbose=verbose, players=players, labels=labels)
        stats[result[0]] += 1

    return stats
# count = 0
# for i in range(9):
#     move(current_player, field, field_comp)
#     if is_win(field):
#         print(f'Вы выиграли!, player = {current_player}')
#         break
#     current_player = 1 if current_player == 2 else 2
# if i == 8:
#     print("Ничья")
print(init(1, verbose=True, players = ['h', 'c']))


# while not is_win(field):
#
#     if is_win(field):
#
#         break
#     move(2,field)
#     # count += count
# # is_win()
# print('Вы выиграли!')