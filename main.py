#!/usr/bin/env python
import time
import telebot
import config
from telebot import types
from Dictionary import list 
#from Dictionary import ListА, ListБ, ListВ, ListГ, ListД, ListЕ, ListЁ, ListЖ, ListЗ, ListИ
#from Dictionary import ListН, ListО, ListП, ListР, ListС, ListТ, ListУ, ListФ, ListХ, ListЙ
#from Dictionary import ListЦ, ListЧ, ListШ, ListЩ, ListЭ, ListЮ, ListЯ, ListК, ListЛ, ListМ

bot = telebot.TeleBot(config.TOKEN)

button_start = "Начать игру"
button_help = "Помощь"
button_feedback = "Обратная связь"
button_stop = "Остановить игру"


@bot.message_handler(commands=['start', 'Помощь', 'help'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/game')
    markup.row('/help')
    markup.row('/feedback')

    bot.send_message(message.chat.id, config.help, reply_markup=markup)


@bot.message_handler(commands=['Связаться', 'feedback'])
def feedback(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/game')
    markup.row('/help')
    markup.row('/feedback')
    bot.send_message(message.chat.id, config.feedback, reply_markup=markup)


@bot.message_handler(commands=['Начать', 'game'])
def game(message):
    markup_off = types.ReplyKeyboardRemove()
    
    bot.send_message(message.chat.id, "Игра началась:", reply_markup=markup_off)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/stop')
    bot.send_message(message.chat.id, config.game_start, reply_markup=markup)

    while True:

        if message.text != "/stop":

            for j in range(0, 10):

                if message.text == list.list[j]:
                    bot.send_message(message.chat.id, 'Я его знаю', reply_markup=markup)

                else:
                    j += 1

                    if j > 51300: 
                        bot.send_message(message.chat.id, config.upss, reply_markup=markup) 
        else:
            break

# Run
if __name__ == '__main__':
    print("Program is start")
    bot.polling(none_stop=True)
    