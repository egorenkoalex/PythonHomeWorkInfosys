# Функция изменения данных сотрудникв справочнике
def update_data(book):
    user_iput_id = int(input('Введите ID сотрудника для изменения данных: '))
    for temp in book:
        if temp["id"] == user_iput_id:
            print("\n" + "=" * 20)
            print("Выберите необходимое действие")
            print('1. Изменить фамилию')
            print('2. Изменить имя')
            print('3. Изменить должность')
            print('4. Изменить телефон')
            print('5. Изменить зарплата')
            step = int(input("Введите номер необходимого действия: "))
            if step == 1:
                temp["last_name"] = input('Введите фамилию нового сотрудника: ')
            elif step == 2:
                temp["first_name"] = input('Введите имя нового сотрудника: ')
            elif step == 3:
                temp["position"] = input('Введите должность нового сотрудника: ')
            elif step == 4:
                temp["phone_number"] = input('Введите телефон нового сотрудника: ')
            elif step == 5:
                temp["salary"] = float(input('Введите зарплату нового сотрудника: '))
    for i in book:
        print(i)
    return book