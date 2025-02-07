num_game_easy = False
num_game_normal = False
num_game_hard = False


def info(message, bot):
    global num, num_game
    text = message.text
    if 'easy' == text:
        num_game_easy = True

    if 'normal' == text:
        num_game_normal = True
    if 'hard' == text:
        num_game_hard = True

    if 'The numbers game' == text:
         bot.send_message(message.chat.id, 'simple task, choose one that right', reply_markup = markup_reply)
    elif num_game_easy:
        if text != str(num) and text in ['1', '2', '3', '4', '5']:

    elif text == str(num) and num_game_easy or num_game_normal or num_game_hard:
        bot.send_message(message.chat.id, f'Yeah, that one, the correct {num}')
        num_game = False

        bot.send_message(message.chat.id, f'Not that one, its was {num}')
        num_game = False

# num = random.randint(1, 5)
#
# markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup_reply.add(types.KeyboardButton('1'))
# markup_reply.add(types.KeyboardButton('2'))
# markup_reply.add(types.KeyboardButton('3'))
# markup_reply.add(types.KeyboardButton('4'))
# markup_reply.add(types.KeyboardButton('5'))