import random

def random_array(n, m, max_value=100):
    array = []
    for i in range(n):
        sub_array = []
        for j in range(m):
            number = random.randint(0, max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array

def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%5d\t" % j, end='')
        print()

def main():
    array = random_array(4, 5)
    print_array(array)

    while True:
        print()
        print("Имеется двумерный массив 4x5.")
        print("Если максимальный элемент в таблице находится в последней строке таблицы,\nто увеличить все элементы первого столбца в 2 раза\n")
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        print()

        if key == '1':
            array = random_array(4, 5)
            print_array(array)

        elif key == '2':
            print("\n--------Выполнение задания--------\n")
            max_value = array[3][0]
            max_row = 3
            max_col = 0

            for row, r in enumerate(array):
                for col, cell in enumerate(r):
                    if cell > max_value:
                        max_value = cell
                        max_row = row
                        max_col = col

            if max_row == 3:
                print("Исходный массив\n")
                print_array(array)
                print()
                print("Максимум исходного массива: ", max_value, "[", max_row + 1, "] [", max_col + 1, "]")

                for row in array:
                    row[0] *= 2

                print("\nУсловие выполнено!\n")
                print("Новый массив")
                print_array(array)
                print()
                print("Максимум нового массива: ", max_value, "[", max_row + 1, "] [", max_col + 1, "]")
            else:
                print("Максимум исходного массива: ", max_value, "[", max_row + 1, "] [", max_col + 1, "]")
                print("Условие не выполнено!")

            print("\n----------Конец задания----------\n")
            input("Нажмите Enter для выхода...")
            break

        elif key == '3':
            exit(0)

if __name__ == '__main__':
    main()
