import telebot
import os

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "नमस्कार! मी तुमचा @jarvisoftejas_bot आहे!")

bot.infinity_polling()
