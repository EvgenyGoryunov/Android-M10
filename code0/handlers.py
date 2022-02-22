from telebot import types

from config import bot


@bot.message_handler(commands=['klava_down'])
def message_main(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/start', '/script', '/test', '/add_text', '/show')
    # keyboard.row('Привет', 'Пока', 'Тест', '🎲 Рандом', )
    bot.send_message(message.chat.id, '---', reply_markup=keyboard)


# прячет клаву
def keyboardRemove(message):
    bot.send_message(message.chat.id, 'удалена', reply_markup=types.ReplyKeyboardRemove())


def def_pass_from_db_handlers():
    """функция пустышка для главной страницы"""
    pass

# вывод кнопок под сообщением
# @bot.message_handler(commands=['klava_under'])
# def start_message(message):
#     print("команда klava_under")
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     markup.add(types.InlineKeyboardButton(text='Три', callback_data=3))
#     markup.add(types.InlineKeyboardButton(text='Четыре', callback_data=4))
#     markup.add(types.InlineKeyboardButton(text='Пять', callback_data=5))
#     bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)


# реагирование на кнопки из чата
# @bot.callback_query_handler(func=lambda call: True)
# def query_handler_1111(call):
#     # выводит сообщение при выборе ответа
#     bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
#     answer = ''
#     if call.data == '111':
#         answer = 'Вы троечник!'
#     elif call.data == '222':
#         answer = 'Вы хорошист!'
#     elif call.data == '333':
#         answer = 'Вы отличник!'
#
#     bot.send_message(call.message.chat.id, answer)
#
#     # удаляет клаву после выбора ответа
#     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                           text="Спасибо за ответ", reply_markup=None)

# запуск команды
@bot.message_handler(commands=['sticker'])
def sticker(message):
    # отправка стикера
    sticker = open("stickers/AnimatedSticker1.tgs", 'rb')
    bot.send_sticker(message.chat.id, sticker)
    print("команда sticker")

@bot.message_handler(commands=['reminders'])
def reminders(message):
    print("команда reminders")
    text = 'reminders ------------- ура ура я красава))))  /reminders'
    bot.reply_to(message, text)


@bot.message_handler(commands=['start', 'help'])
def main_menu(message):
    text = ('Добро пожаловать, {0.first_name}!'
            '\n\nЯ - {1.first_name}, умный ТелеграмБот'            
            '\n\nГотов всегда помочь')
            # '\n\nГотов помощь по следующим темам:'
            # '\nдосуг  -  /leisure'
            # '\nумные напоминания  -  /reminders'
            # '\nактивировать нижнюю клавиатуру  -  /klava_down'
            # '\nактивировать под сообщением  -  /klava_under'
            # '\nвывести стикер  -  /sticker')
    bot.send_message(message.chat.id, text.format(message.from_user, bot.get_me()), parse_mode='html')
    message_main(message)


#
#

#
