import telebot
from telebot import types
TOKEN = '733447764:AAHvEMWPaumZ-lXlkiwyhAb6ttYHvVcZpSs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    name = message.from_user.first_name
    bot.send_message(cid, "Bienvenidx <b>" + name + "</b>!" ", este es el bot de la Delegación de Estudiantes de Teleco, para saber que puede hacer el bot usa el comando /help", parse_mode="HTML")

@bot.message_handler(commands=['help'])
def help_message(message):
    msg = "Actualmente estos son los comandos disponibles para usar este bot /start /help /curso"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['documento'])
def send_pdf(message):
    doc = open('/home/cristian/Downloads/document.pdf', 'rb')
    bot.send_document(message.chat.id, doc)
    doc.close()

bot.polling()
