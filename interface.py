import delete
import write
import print1
import edit
import search
import import_file
import telebot

token='5868181298:AAF3AtbfFO_Lhb_LqZs3tTwDE4hU-xfO1t8'                        
bot=telebot.TeleBot(token)


# value = int(input("Выберите действие: "))


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'База данных сотрудников.\n')
    bot.send_message(m.chat.id, '1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Импорт данных.\n7. Выход.\n')

@bot.message_handler(content_types=["text"])
def after_text(message):
    if message.text == "1":
        user_mes = print1.print_all_to_console('employees.csv')
        for i in user_mes:
            bot.send_message(message.chat.id, i)
    # elif message.text == "2":
    #     user_mes = write.New_Entry()
    #     bot.send_message(message.chat.id, user_mes)
    # elif message.text == "3":
    #     user_mes = search.Search_Entry('employees.csv')
    #     bot.send_message(message.chat.id, user_mes)


    else:
        bot.send_message(message.chat.id, 'Я на связи. Напиши мне что-нибудь )')

#     if value == 1:
#         print1.print_all_to_console('employees.csv')
#     elif value == 2:
#         write.New_Entry()
#     elif value == 3:
#         search.Search_Entry('employees.csv')
#     elif value == 4:
#         edit.Edit_Entry('employees.csv')
#     elif value == 5:
#         delete.delete_str('employees.csv')
#     elif value == 6:
#         import_file.import_file(input("Введите зазвание файла: "), 'employees.csv')
#     elif value == 7:
#         break


bot.polling(none_stop=True, interval=0)


