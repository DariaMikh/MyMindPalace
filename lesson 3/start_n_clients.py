from subprocess import Popen, CREATE_NEW_CONSOLE

p_list = []

while True:
    user = input("Запустить несколько клиентов (s) / "
                 "Закрыть клиентов и выйти(x)\n")
    if user == 's':
        read_or_write = input("На чтение (r) /"
                              "На запись (w)\n")
        number = int(input("Сколько?\n"))
        for i in range(number):
            p_list.append(Popen('python client.py --mode ' + read_or_write,
                                creationflags=CREATE_NEW_CONSOLE))
        print('Запущено {} клиентов.'.format(number))

    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()
        break
