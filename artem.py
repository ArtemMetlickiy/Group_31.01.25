import re
import wikipedia
from telebot.util import content_type_media

wiki = True
def artem(message, bot, types):
    global wiki
    text = message.text
    if wiki:
        bot.send_message(message.chat.id, get_wiki())
    if "Википедия" == text:
        bot.send_message(message.chat.id, "Скажи что тебе найти?")

wikipedia.set_lang("ru")
def get_wiki(word):
    try:
        w = wikipedia.page(word)
        wikitext = w.content[:1000]
        wiki_list = wikitext.split(".")
        wiki_list = wiki_list[:-1]
        wiki_result = ""
        for i in wiki_list:
            if not ("==" in i):
                wiki_result = wiki_result + i + "."
            else:
                break
        wiki_result = re.sub('\([^()]*\)', '', wiki_result)

        return wiki_result
    except Exception as error:
        return "Error"
