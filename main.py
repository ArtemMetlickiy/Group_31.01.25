print("Hello")
import telebot
token = "7925900642:AAG5BuVLwIvadstEaGgx_pzdySwnJwPxhoI"
text = ""
ling = ""
clients = []
admins = [6210349680]
bot=telebot.TeleBot(token)





@bot.message_handler(commands=["start"])
def start_message(message):
    if message.chat.id in admins:
        bot.send_message(message.chat.id, "привет")
    else:
        clients.append(message.chat.id)
bot.infinity_poling()



