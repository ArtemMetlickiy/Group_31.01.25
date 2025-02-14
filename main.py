from telebot import types
from dima import dima_adm
from dima import dima_cln
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
        dima_adm(message, bot, types)
    else:
        clients.append(message.chat.id)
        dima_cln(message, bot, types)
bot.infinity_poling()


