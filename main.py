from telebot import types
from dima import dima_adm
from dima import dima_cln
import telebot
from text_daniil import danniil
from telebot import types
from artem import artem
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


@bot.message_handler(commands=["text_daniil"])
def  start_mesaage (message):
    danniil(message)




@bot.message_handler(commands=["artem"])
def art(message):
    artem(message, bot, types)
    dima_cln(message, bot, types)

@bot.message_handler(commands=["dima"])
def dima(message):
    dima_cln(message, bot, types)
    dima_adm(message, bot, types)
bot.infinity_poling()

