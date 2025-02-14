def dima_adm(message, bot, types):
    bot.send_message(message.chat.id, "Команды ботов:\n"
        "/edit_message - Команда для редактирования сообщения рассылки.\n"
        "/edit_link - Команда для редактирования ссылки.\n"
        "/send или /send_message - начать рассылку.\n"
        "/help - Помощь.")
def dima_cln(message, bot, types):
    bot.send_message(message.chat.id, "Команды ботов:\n"
                                      "/help - Помощь.\n"
                                      "/poleznaya_komanda - очень полезная команда.\n"
                                      "/ya_ne_znay_chto_pisat - для людей которые не знаю что писать")
