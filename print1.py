def print_all_to_console(file):
    messeg = []
    with open(file, encoding="utf-8") as data:
        for line in data:
            messeg.append(line.replace(',', ' '))
    return messeg      

