import telebot
import config

bot = telebot.TeleBot("5790997230:AAEBzn1UgKTkXWsaLRl8L6nqZuLgHCudKao")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Шалом, {0.first_name}!".format(message.from_user, bot.get_me()))

@bot.message_handler()
def get_user_text(message):
    if message.text == "Кайф респект" or "Привет":
        bot.send_message(message.chat.id, "Приветствую", parse_mode='html')
    elif message.text == "хай":
        bot.send_message(message.chat.id, "Что ты несешь?", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Пошел ты, козел!", parse_mode='html')

@bot.message_handler(content_types=["document"])
def fourth(message):
    bot.send_message(message.chat.id, "Не нужно присылать мне документы, я бездушный код, а не твой босс")

@bot.message_handler(content_types=["audio"])
def fourth(message):
    bot.send_message(message.chat.id, "Выключи это дерьмо, немедленно!")

bot.polling(none_stop=True)