import telebot
import config
from urllib.request import urlopen

bot = telebot.TeleBot(config.TG_API_TOKEN)

@bot.message_handler(commands=['start'])
def get_user_photo(message):
    if message.text == '/start':
        photo1 = urlopen('https://cdn.culture.ru/images/69b64b45-dc21-5230-951c-9722db631cd0')
        bot.send_photo(message.chat.id, photo1)

bot.infinity_polling()