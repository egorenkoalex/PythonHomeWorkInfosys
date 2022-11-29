# Функция поиска абонента в справочнике
def search_name(phonebook):
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника по ID")
    print("2. Найти сотрудника по Фамилии")
    print("3. Найти сотрудника по Имени")
    print("4. Найти сотрудника по должности")

    step = int(input("Введите номер необходимого действия: "))

    if step == 1:
        id_user = int(input("Введите ID сотрудника: "))
        for employee in phonebook:
            if id_user == employee['id']:
                print(employee)

    elif step == 2:
        last_name = input("Введите фамилию сотрудника: ")
        for employee in phonebook:
            if last_name in employee['last_name']:
                print(employee)
    elif step == 3:
        first_name = input("Введите имя сотрудника: ")
        for employee in phonebook:
            if first_name in employee['first_name']:
                print(employee)
    elif step == 4:
        position = input("Введите имя сотрудника: ")
        for employee in phonebook:
            if position in employee['position']:
                print(employee)
    else:
        print("Не корректный ввод.")