import telebot
import config


bot = telebot.TeleBot(config.TG_API_TOKEN)



bot.infinity_polling()