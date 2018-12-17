import telebot
from telebot import types
import time

TOKEN = '733447764:AAFPAT2C7I4MjbDz8bG34Twyzam3Uwyq2-k'

AYUDA = '/help'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hola, Bienvenido al bot de la Delegación de Estudiantes de Teleco")

@bot.message_handler(commands=['help'])
def help_message(message):
    msg = "Actualmente estos son los comandos disponibles para usar este bot /start /help"
    bot.send_message(message.chat.id, msg)

bot.polling()
