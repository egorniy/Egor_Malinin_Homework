import sqlite3
def show_menu(level):
    if level == 1:
        return '1New 2.Work with DB 0.Exit'
    else:
        return '1. Select 2.Update 3.Delete 4.Insert 0.Exit to menu'
menu_level = 1
connection = None
cursor = None
while True:
    answer = input(show_menu(menu_level))
    if menu_level == 1:
        if answer == '0':
            break
        elif answer == '2':
            menu_level == 2
        elif answer == '1':
            path = input(' Введите путь')
            if connection:
                connection.close()
            if cursor:
                cursor.close()
            connection=sqlite3.connect(path)
            cursor= connection.cursor()
        elif menu_level == 2:
            ans = input(show_menu(2))
            if ans == '1':
                select = input('SELECT:')
                fr = input('FROM:')
                where = input ('WHERE:')
            if cursor:
                com = 'SELECT %S FROM %S WHERE %S;' %(select,fr,where)
                cursor.execute(com)
                print(cursor.fetchall())
            elif ans == '0':
                 menu_Level = 1 
