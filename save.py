# Функция сохранения  справочника сотрудников в формате на выбор пользователя
import csv
import json
from pathlib import Path


def save_file(book_list):
    save_book = input('Введите имя сохраняемого файла: ')
    if save_book[-3:] == 'csv':
        with open(Path.cwd() / save_book, 'w+', encoding='utf-8') as save_employyee_book:
            csv_writer = csv.writer(save_employyee_book, lineterminator='\r')
            for employee in book_list:
                csv_writer.writerow(employee.values())

    elif save_book[-3:] == 'son':
        with open(Path.cwd() / 'database.json', 'w+', encoding='utf-8') as save_employyee_book:
            for employee in book_list:
                save_employyee_book.write(json.dumps(employee) + '\n')

    else:
        print('Неверный формат файла!')