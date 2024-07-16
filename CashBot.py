import telebot

TOKEN = telebot.TeleBot('7474929055:AAGAiuFuh8zA04zwt7w-c1aqXxJYZqFN5rg')

from telebot import types

@TOKEN.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  markup.add(button_yes)
  TOKEN.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

TOKEN.infinity_polling()