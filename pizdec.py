import telebot

bot = telebot.TeleBot('6551171127:AAHETvh54LIaijCuHAyMXPPl6Rcmw_ItA6M')


bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова хохлы')


bot.polling(none_stop=True)
