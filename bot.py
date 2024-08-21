from telebot import TeleBot, types

TOKEN = '7506589737:AAGwAEy6KV934rSVERRfUebTNU2vNQIzTfM'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Ютуб')
    btn2 = types.KeyboardButton('Фикбук')
    btn3 = types.KeyboardButton('Ватпад')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Гитхаб')
    btn5 = types.KeyboardButton('Инсаграм')
    btn6 = types.KeyboardButton('Анонимные вопросы')
    markup.row(btn4, btn5, btn6)
    btn7 = types.KeyboardButton('Тикток')
    btn8 = types.KeyboardButton('Дискорд сервер')
    markup.row(btn7, btn8)
    bot.send_message(message.chat.id, f'Здравствуй {message.from_user.first_name}! Тебя приветствует создатель фф и разработчик различных игр/программ. /n Здесь ты сможешь посмотреть все мои ссылки на каналы, а так же на бусты). ', reply_markup=markup)


bot.polling(none_stop=True)
