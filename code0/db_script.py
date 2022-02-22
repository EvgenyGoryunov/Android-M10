import datetime
import os
import sqlite3

from telebot import types

from config import bot
from handlers import message_main

isRunning = False

con = sqlite3.connect('database.db', check_same_thread=False)
cursor = con.cursor()

"""********************************************** КОМАНДЫ ИЗ ЧАТА **************************************************"""


@bot.message_handler(commands=['script'])
def add_title_step_0(message):
    """запуск сценария по созданию скрипта"""
    msg = bot.send_message(message.chat.id, 'Введите название заметки')
    bot.register_next_step_handler(msg, add_title_db_scripts)
    # print("add_title_step_0\n")


def buttons_scripts_inline(message):
    """выводит клавиатуру под сообщением"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text='Добавить описание', callback_data='Добавить описание'))
    markup.add(types.InlineKeyboardButton(text='Добавить фото', callback_data='Добавить фото'))
    markup.add(types.InlineKeyboardButton(text='Завершить', callback_data='Завершить'))
    bot.send_message(message.chat.id, text="Выберите следующее действие", reply_markup=markup)
    # print("buttons_scripts_inline\n")


@bot.callback_query_handler(func=lambda call: True)
def add_step_11(call):
    bot.answer_callback_query(callback_query_id=call.id, text='--')
    if call.data == 'Добавить описание':
        msg = bot.send_message(call.message.chat.id, 'Введите сообщение с описанием')
        bot.register_next_step_handler(msg, add_text_db_scripts)
    elif call.data == 'Добавить фото':
        msg = bot.send_message(call.message.chat.id, 'Прикрепите фото к сообщению')
        bot.register_next_step_handler(msg, add_photo_db_scripts)
    elif call.data == 'Завершить':
        message_main(call.message)
    # print("add_step_11\n")


"""****************************************** РАБОТА С БАЗОЙ ДАННЫХ **********************************************"""


def add_title_db_scripts(message):
    """создает первую записи в бд: вносит ид_сообщения,
    ид_юзера, время создания и название скрипта"""
    try:
        global id_msg
        global id_chat
        bot.reply_to(message, "Название успешно сохранено")
        id_msg = message.id
        id_chat = message.chat.id
        id_user = str(message.from_user.id)[:5]
        time_create = datetime.date.today().strftime("%Y-%m-%d")
        title = message.text
        cursor.execute('INSERT INTO scripts (id_msg, id_user, time_create, title) VALUES (?, ?, ?, ?)',
                       (id_msg, id_user, time_create, title))
        con.commit()
        buttons_scripts_inline(message)
        # print('add_title_db_scripts\n')
    except Exception as e:
        bot.reply_to(message, 'ошибка в модуле: add_title_db_scripts')


def add_text_db_scripts(message):
    """добавляет текст в бд"""
    try:
        if message.content_type == 'text':
            text = message.text
            empty_step = find_next_empty_step(id_msg)
            cursor.execute(f'UPDATE scripts SET {empty_step} = ? WHERE id_msg = ?', (text, id_msg))
            con.commit()
            bot.reply_to(message, "Описание успешно добавлено")
            buttons_scripts_inline(message)
            # print('add_text_db_scripts\n')
        else:
            bot.reply_to(message, 'Это не текст, пришлите пожалуйста текст!')
            buttons_scripts_inline(message)
            # print('else текст------------------------------------------')
    except Exception as e:
        bot.reply_to(message, 'ошибка в модуле: add_text_db_scripts')


def add_photo_db_scripts(message):
    """добавляет локальный путь фото в бд"""
    try:
        path_photo = add_photo_local(message)
        if path_photo is not None:
            empty_step = find_next_empty_step(id_msg)
            cursor.execute(f'UPDATE scripts SET {empty_step} = ? WHERE id_msg = ?', (path_photo, id_msg))
            con.commit()
            bot.reply_to(message, "Фото успешно добавлено")
            buttons_scripts_inline(message)
            # print('add_photo_db_scripts\n')
    except Exception as e:
        bot.reply_to(message, 'ошибка в модуле: add_photo_db_scripts')


def find_next_empty_step(id_msg):
    """получает имя ближайшей свободной колонки в бд, например step7"""
    try:
        cursor.execute('SELECT * FROM scripts WHERE id_msg = ?', (id_msg,))  # получили строку по ид_собщения
        row_from_db_scripts = cursor.fetchone()
        index_empty_column = row_from_db_scripts.index(None)  # нашли индекс ближайшей свободной колонки
        con.row_factory = sqlite3.Row
        cursor1 = con.execute('select * from scripts')
        row = cursor1.fetchone()
        col_list = row.keys()  # получили список имен колонок таблицы
        name_empty_column = col_list[index_empty_column]  # получили имя ближайшей свободной колонки
        # print('find_next_empty_step\n')
        return name_empty_column
    except Exception as e:
        bot.reply_to(id_chat, 'oooops')


def scr_save(message):
    print('scr_save')


def del_text_db_scrscripts(message):
    print('del_text_db_scripts')


def del_text_db_scripts(message):
    print('del_text_db_photo')


"""*************************************** ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ *************************************************"""


@bot.message_handler(commands=['test'])
def message_main_1(message):
    """тестовая функция (для экспериментов), есть отдельная кнопка на гл.нижней клавиатуре"""
    times = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    print(times)


def add_photo_local(message):
    """добавляет фото в локальную папку"""
    try:
        keyboardRemove(message)
        if message.content_type == 'photo':
            # print('if')
            id_photo = bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(id_photo.file_path)
            filename, file_extension = os.path.splitext(id_photo.file_path)
            path_photo = "db_files/photos/" + str(message.from_user.id) + '_' + str(message.id) + file_extension
            with open(path_photo, 'wb') as new_file:
                new_file.write(downloaded_file)
            # print('add_photo_local\n')
            return path_photo
        else:
            bot.reply_to(message, 'Это не фотография, пришлите пожалуйста фото!')
            buttons_scripts_inline(message)
            # print('add_photo_local else------------------------------------------\n')
            return None
    except Exception as e:
        bot.reply_to(message, 'ошибка в модуле: add_photo_local')


"""*************************************** ВРЕМЕННО НЕ ЗАДЕЙСТВОВАН ***********************************************"""


def buttons_scripts(message):
    """выводит клавиатуру внизу экрана"""
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Текст', '/Фото', '/Завершить', '/Главное меню')
    msg = bot.send_message(message.chat.id, 'Выберите, что хотите добавить текст/фото?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, add_step_1)
    # print('buttons_scripts')


@bot.message_handler(commands=['Текст', 'Фото'])
def add_step_1(message):
    """реакция на кнопки нижней клавиатуры"""
    msg = bot.send_message(message.chat.id, '-')
    if message.text == '/Текст':
        bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(msg, add_text_db_scripts)
    elif message.text == '/Фото':
        bot.send_message(message.chat.id, 'Прикрепите фото')
        bot.register_next_step_handler(msg, add_photo_db_scripts)
    elif message.text == '/Завершить':
        bot.register_next_step_handler(msg, scr_save)
    elif message.text == '/Главное меню':
        message_main(message)
    # print('add_step_1')


def keyboardRemove(message):
    """удаляет нижнюю клавиатуру"""
    bot.send_message(message.chat.id, '---', reply_markup=types.ReplyKeyboardRemove())


def def_pass_from_db_scripts():
    """функция пустышка для главной страницы"""
    pass


"""
удаляет клаву после выбора ответа, вставляется в самый низ под инлайн клаву
bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text="Спасибо за ответ", reply_markup=None)
"""
