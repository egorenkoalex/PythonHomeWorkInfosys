import open as op
import save as sav
import search as sea
import view as vie
import add_employee as adsub
import selection as selec
import dell_employee as dellit
import  update_data as updat


# Вывод открытого справочника
def printer(book_list):
    global book
    book = book_list
    for i in book:
        print(i)

    return book


# Функция реакции на выбор пользователя
def step(step_next):
    if step_next == 1:
        printer(op.open_file())
        step(vie.show_menu())
    elif step_next == 2:
        try:
            sea.search_name(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 3:
        try:
            selec.find_employees_by_salary_range(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 4:
        try:
            selec.find_employees_by_position(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 5:
        try:
            adsub.add_employee(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 6:
        try:
            dellit.dell_employee(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 7:
        try:
            updat.update_data(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 8:
        try:
            sav.save_file(book)
            step(vie.show_menu())
        except:
            print('Сначала откройте файл')
            step(vie.show_menu())
    elif step_next == 9:
        exit()