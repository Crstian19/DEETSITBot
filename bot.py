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
    msg = "Actualmente estos son los comandos disponibles para usar este bot /start /help /apuntes /examenes /calendario"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['calendario'])
def calendar(message):
    msg = "http://teleco.upct.es/wp-content/uploads/2018/07/calendarioacademico1819.pdf"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['examenes'])
def exams(message):
    msg = "http://teleco.upct.es/wp-content/uploads/2018/12/CalendarioFebrero_AULAS.pdf"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['apuntes'])
def gen_markup(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=2)
    itembtn1 = types.KeyboardButton('Primero')
    itembtn2 = types.KeyboardButton('Segundo')
    itembtn3 = types.KeyboardButton('Tercero (GIT)')
    itembtn4 = types.KeyboardButton('Cuarto (GIT)')
    itembtn5 = types.KeyboardButton('Tercero (GIST)')
    itembtn6 = types.KeyboardButton('Cuarto (GIST)')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(message.chat.id, "Elige un curso:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text== 'Primero')
def curso_primero(message):
    subject_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Cálculo 1')
    itembtn2 = types.KeyboardButton('Física')
    itembtn3 = types.KeyboardButton('Álgebra')
    itembtn4 = types.KeyboardButton('F.Programación')
    subject_markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Elige una asignatura:", reply_markup=subject_markup)

@bot.message_handler(func=lambda message: message.text== 'Cálculo 1')
def calculo1(message):
    msg = "https://drive.google.com/open?id=0B7OtwXyjfmOZeFU4RUNZVmwtT2M"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Álgebra')
def algebra(message):
    msg = "https://drive.google.com/file/d/0B7OtwXyjfmOZcUl3ZF9MMlV2NE0/view?usp=sharing"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Física')
def algebra(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'F.Programación')
def algebra(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

bot.polling()
