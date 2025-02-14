import telebot
from telebot import types
from dima import dima_adm
from dima import dima_cln
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

@bot.message_handler(commands=["dima"])
def dima(message):
    dima_cln(message, bot, types)
    dima_adm(message, bot, types)
bot.infinity_poling()

