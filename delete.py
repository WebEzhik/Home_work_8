def delete_str(file):

    print(f'Введите имя для удаления данных о нём')
    name = input()
    lines = []
    
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if not name in line: lines += line

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)
        
    print('Удаление произведено...')


