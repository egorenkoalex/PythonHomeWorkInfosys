# Добавления абонента в справочник сотрудников
def add_employee(book):
    temp = {}
    temp["id"] = int(input('Введите ID нового сотрудника: '))
    temp["last_name"] = input('Введите фамилию нового сотрудника: ')
    temp["first_name"] = input('Введите имя нового сотрудника: ')
    temp["position"] = input('Введите должность нового сотрудника: ')
    temp["phone_number"] = input('Введите телефон нового сотрудника: ')
    temp["salary"] = float(input('Введите зарплату нового сотрудника: '))
    book.append(temp)
    for item in book:
        print(item)
    return book