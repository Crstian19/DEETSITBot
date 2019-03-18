import telebot
from telebot import types
TOKEN = 'BOT TOKEN'
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
    itembtn5 = types.KeyboardButton('F.Computadores')
    itembtn6 = types.KeyboardButton('Gestión de empresas')
    itembtn7 = types.KeyboardButton('Cálculo 2')
    itembtn8 = types.KeyboardButton('Sistemas y Circuitos')
    itembtn9 = types.KeyboardButton('Estadística')
    itembtn10 = types.KeyboardButton('F.Telemática')

    subject_markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)
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
def fisica(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'F.Programación')
def programacion(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Física')
def fisica(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Física')
def fisica(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Física')
def fisica(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Física')
def fisica(message):
    msg = "Próximamente..."
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: message.text== 'Segundo')
def curso_segundo(message):
    subject_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Redes y Servicios')
    itembtn2 = types.KeyboardButton('Conmutación')
    itembtn3 = types.KeyboardButton('Ondas Electromagnéticas')
    itembtn4 = types.KeyboardButton('Sistemas Lineales')
    itembtn5 = types.KeyboardButton('Componentes y dispositivos electrónicos')


    subject_markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9)
    bot.send_message(message.chat.id, "Elige una asignatura:", reply_markup=subject_markup)

bot.polling()
