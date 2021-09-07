import os
import time
import keyboard
def main():
    print("Выберите команду:")
    print("1.Завершение работы")
    print("2.Сон")
    print("3.Перезагрузка")
    print("4.Выйти из системы")
    print("5.Заблокировать клавиатуру")
    a = int(input("Номер команды:"))
    print("Через сколько секунд?")
    local_time = float(input())
    local_time = local_time * 1
    if a == 5:
        block_time = input("Укажите время блокировки клавиатуры (в секундах): ")
        print(block_time)
    time.sleep(local_time)
    if a == 1:
        os.system("shutdown /p")
    elif a == 2:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif a == 3:
        os.system('shutdown' '-r' '-t' '0')
    elif a == 4:
        os.system("shutdown -1")
    elif a == 5:
        for i in range(150):
            keyboard.block_key(i)
        time.sleep(int(block_time))
        for i in range(150):
            keyboard.unblock_key(i)
        print("Клавиатуру разблокировано!")
    # Выход
    # из
    # программы:
    if input("Type \"y\" to exit: ") == "y":
        return 0
    else:
        main()


main()

