# Функция открытия файла
import csv
import json
from pathlib import Path


def open_file():
    openen = input('Введите адрес файла: ')
    if openen[-3:] == 'csv':
        employee = []
        with open(Path.cwd() / openen, 'r', encoding='utf-8') as fin:
            csv_reader = csv.reader(fin)
            for row in csv_reader:
                temp = {}
                temp["id"] = int(row[0])
                temp["last_name"] = row[1]
                temp["first_name"] = row[2]
                temp["position"] = row[3]
                temp["phone_number"] = row[4]
                temp["salary"] = float(row[5])
                employee.append(temp)
        return employee
    elif openen[-3:] == 'son':
        employee = []
        with open(Path.cwd() / openen, 'r', encoding='utf-8') as fin:
            for line in fin:
                temp = json.loads(line.strip())
                employee.append(temp)
        return employee
    else:
        print('Неверный формат файла!')