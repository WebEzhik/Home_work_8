def Search_Entry(file):

    print(f'Введите имя для поиска: ')
    name = input()
   
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if name in line: 
                    print(line)