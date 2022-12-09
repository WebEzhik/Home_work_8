import telebot



def Search_Entry(file):
    @bot.message_handler(commands=["text"])
    def after_text(message):
        bot.send_message(message.chat.id, 'Введите имя для поиска: ')
        name = input()
   
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if name in line: 
                    print(line)