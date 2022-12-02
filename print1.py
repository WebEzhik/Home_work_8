def print_all_to_console(file):

    with open(file, encoding="utf-8") as data:
        for line in data:
            print(line.replace(',', ' '))
            
