# Удаление сотрудника из справочника
def dell_employee(book):
    id_user = int(input("Введите ID сотрудника для удаления: "))
    for index, employee in enumerate(book):
        if id_user == employee['id']:
            del book[index]
    for item in book:
        print(item)
    return book



