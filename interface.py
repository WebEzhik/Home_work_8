import delete
import write
import print1
import edit
import search
import import_file

while True:
    print("База данных сотрудников.\n")
    print('1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Импорт данных.\n7. Выход.\n')

    value = int(input("Выберите действие: "))
    print(value)
    if value == 1:
        print1.print_all_to_console('employees.csv')
    elif value == 2:
        write.New_Entry()
    elif value == 3:
        search.Search_Entry('employees.csv')
    elif value == 4:
        edit.Edit_Entry('employees.csv')
    elif value == 5:
        delete.delete_str('employees.csv')
    elif value == 6:
        import_file.import_file(input("Введите зазвание файла: "), 'employees.csv')
    elif value == 7:
        break





