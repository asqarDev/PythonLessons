
import telebot
from translate import to_latin, to_cyrillic

TOKEN = '5301429201:AAGxpQGvB0eYsZYx1rbRa6XgKfY8q4sneCM'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = "Assalomu aleykum, Xush kelibsiz!"
	javob += "\nMatin kiriting: "
	bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	natija = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	bot.reply_to(message, natija(msg))

bot.infinity_polling()





# matn = input("Matnni kiriting: ")
#
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))


