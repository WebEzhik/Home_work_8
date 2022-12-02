def import_file(file, file_baza):
    lines = []

    with open(file_baza, encoding="utf-8") as data:
        for line in data:
            lines += line.replace(',', ' ')

    with open(file, encoding="utf-8") as data:
        for line in data:
            lines += line.replace(',', ' ')
    
    with open(file_baza, 'w', encoding="utf-8") as data:
        data.writelines(lines)