import os
import random
import time
import string
from datetime import datetime


# Функция выбора размера массива
def choose_array_size():
    # Создаю кортеж возможных размеров массива:
    array_size = (10, 100, 1000, 10_000, 1_000_000_000, 10_000_000_000)
    print("Available array size: 1)10, 2)100, 3)1000, 4)10_000, 5)1_000_000_000, 6)10_000_000_000")
    # Создаю переменную choice для выбора размера массива:
    try:
        choice = input("Choose size of an array(1-6):")
        choice = int(choice) - 1
    # Создаю исключения ValueError, IndexError:
    except ValueError:
        print("Error!")
        choose_array_size()
    except IndexError:
        print("Error!")
        choose_array_size()
    size = array_size[choice]
    return size


def manual_fill_array(choice, array_size):
    def tempinput(choice):
        if choice == 1:
            try:
                temp = int(input())
            except ValueError:
                print("Wrong type!")
                tempinput(choice)
        if choice == 2:
            try:
                temp = float(input())
            except ValueError:
                print("Wrong type!")
                tempinput(choice)
        # ДОПИЛИТЬ ВВОД СИМВОЛОВ
        if choice == 3 or choice == 4:
            try:
                temp = input()
                return temp
            except ValueError:
                print("Wrong type!")
                tempinput(choice)



    array = list()
    # Условная конструкция для определения типа массива:
    if choice == 1:
        arr_type = "int"
    elif choice == 2:
        arr_type = "float"
    elif choice == 3:
        arr_type = "char"
    elif choice == 4:
        arr_type = "mixed"
    # Условная конструкция для выбора типа массива:
    print("Please input array of choosen type:")
    for i in range(array_size):
        array.append(tempinput(choice))
    print(f"Random {arr_type} array: \n {array}")
    return array


# Функция заполнения массива значениями:
def auto_fill_array(choice, array_size):
    # Подфункция для создания массива смешанного типа:
    def mixed(mix_choice):
        if mix_choice == 1:
            return random.randint(1, 100)
        if mix_choice == 2:
            return random.random()
        if mix_choice == 3:
            return array.append(random.choice(string.ascii_letters))


    array = list()
    # Условная конструкция для выбора типа массива:
    if choice == 1:
        print("Generating random int array..")
        for i in range(array_size):
            array.append(random.randint(1, 100))
        print(f"Random int array: \n {array}")

    if choice == 2:
        print("Generating random float array")
        for i in range(array_size):
            array.append(random.random())
        print(f"Random float array: \n {array}")
    if choice == 3:
        print("Generating random char array")
        for i in range(array_size):
            array.append(random.choice(string.ascii_letters))
        print(f"Random char array: \n {array}")
    if choice == 4:
        print("Generating random mixed array..")
        for i in range(array_size):
            mixed_choice = random.randint(1, 3)
            array.append(mixed(mixed_choice))
        print(f"Random mixed array: \n {array}")
    return array

# Вычисление времени создания массива
NOW = datetime.now()
CURRENT_TIME = datetime.today()

def main():
    # НАЧАЛО РАБОТЫ ПРОГРАММЫ:
    # Выбор типа данных массива:
    print("Array type: ")
    choice = input("1 - int, 2 - float, 3 - char, 4 - mixed: ")
    # Выбор типа заполнения массива:
    print("Выберите тип заполнения: ")
    inputType = input("(1 - Ручной, 2 - Автоматический): ")
    if int(inputType) == 1:
        try:
            start_time = time.time()
            arrayy = manual_fill_array(int(choice), choose_array_size())
            print(f"Generation time: {time.time() - start_time}")
            print("Array length: " + str(len(arrayy)))
            print(f"Generation date: {CURRENT_TIME}")
        except ValueError:
            print("Error!")
    elif int(inputType) == 2:
        try:
            start_time = time.time()
            arrayy = auto_fill_array(int(choice), choose_array_size())
            print(f"Generation time: {time.time() - start_time}")
            print("Array length: " + str(len(arrayy)))
            print(f"Generation date: {CURRENT_TIME}")
        except ValueError:
            print("Error!")

    # Создаём файл статистики:
    stats = open('statistics.txt', 'a')
    # Открываем файл, считываем количество строк для определения порядкового номера записи:
    with open('statistics.txt') as f:
        lines_num = len(f.readlines())
    # Переменная-счётчик порядкового номера записи файла статистики:
    stats_record_num = lines_num + 1

    # Запись в файл статистики:
    stats.write(f"Array number {stats_record_num}; "
                f"Generation time: {time.time() - start_time}; "
                f"Array length: {str(len(arrayy))}; "
                f"Generation date: {CURRENT_TIME}; "
                f"{arrayy};\n")
    stats.close()

#   Открыть файл статистики:
    if input("Type \"y\" to show statistics:") == "y":
        os.system("type statistics.txt")
#   Выход из программы:
    if input("Type \"y\" to exit: ") == "y":
        return 0
    else:
        main()


main()

