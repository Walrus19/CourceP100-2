import os
field = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
for row in field:
    for cell in row:
        print(cell, end=" ")
    print()

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


def move(current_player,field):
        c = 0
        position = [0 , 0]
        # os.system('cls||clear')
        position = input(f'Введите позицию игрок ({current_player}):').split(sep=',')
        position = [int(el) for el in position]

        # print(position)
        if current_player == 1:
            if field[position[0]][position[1]] == '[ ]':
                field[position[0]][position[1]] = ' x '
            else:
                print('Ошибочный ввод')
                move(current_player, field)
                c = 1
        else:
            if field[position[0]][position[1]] == '[ ]':
                field[position[0]][position[1]] = ' 0 '
            else:
                print('Ошибочный ввод')
                move(current_player, field)
                c = 1
        if c == 0:
            for row in field:
                for cell in row:
                    print(cell, end=" ")
                print()


# count = 0
print(is_win(field))
while is_win(field) is False:
    move(1,field)
    move(2,field)
    # count += count
# is_win()
print('Вы выиграли!')