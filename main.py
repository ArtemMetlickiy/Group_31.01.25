
import telebot
from text_daniil import danniil
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

@bot.message_handler(commands=["text_daniil"])
def  start_mesaage (message):
    danniil(message)

bot.infinity_poling()


