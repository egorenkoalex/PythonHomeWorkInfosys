def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    for item in result:
        print(item)


def get_salary_range():
    lo = float(input('Введите нижнюю границу поиска: '))
    hi = float(input('Введите верхнюю границу поиска: '))
    return lo, hi



def find_employees_by_position(employees: list) -> list:
    result = []
    pos = input('Введите наименование должности: ')
    for employee in employees:
        if pos in employee["position"]:
            result.append(employee)
    for item in result:
        print(item)
