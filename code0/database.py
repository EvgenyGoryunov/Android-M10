import datetime
import os
import sqlite3

from config import bot

conn = sqlite3.connect('database.db', check_same_thread=False)  # устанавливаем подключение к базе данных
cursor = conn.cursor()  # создаем курсор для работы с таблицей


# вносит данные пользователя в бд (либо отказываем, если уже зарегистрирован ранее)
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, message):
    # проверка на наличие ид_пользователя в бд
    user_id_exist = cursor.execute('SELECT * FROM test WHERE user_id=?', (user_id,))
    # если пользователь отсутствует, то выполнить код (добавление в бд)
    if user_id_exist.fetchone() is None:
        cursor.execute('INSERT INTO test '
                       '(user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                       (user_id, user_name, user_surname, username))
        conn.commit()  # команда, чтоб применить изменения (внести инфу в бд и сохранить бд)
        print('Привет! Ваше имя добавленно в базу данных!')
    # если человек уже был зарегистрирован в бд, то выполнить данный код
    else:
        bot.send_message(message.from_user.id, 'Вы уже были зарегистрированы ранее')
        print('Стоп!"!! Вы уже были зарегистрированы ранее!')


# добавляет пользователя в бд (если уже есть в базе, то отлавливает исключение и выдает сообщение)
@bot.message_handler(commands=['reg'])
def reg(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    mes = message
    db_table_val(user_id=us_id,
                 user_name=us_name,
                 user_surname=us_sname,
                 username=username,
                 message=mes)


# нажимаем на команду создания заметки, получаем сообщение и переходим к след.этапу
@bot.message_handler(commands=['add_text'])
def add_text(message):
    # global isRunning
    # if not isRunning:
    msg = bot.send_message(message.chat.id, 'Введите пункты вашего сообещния')
    bot.register_next_step_handler(msg, add_text_2)
    # isRunning = True


def add_text_2(message):
    times = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    db_add_text(message.id, message.from_user.id, message.from_user.first_name, message.from_user.last_name, times,
                message.text)
    msg = bot.send_message(message.chat.id, 'Список успешно внесен, добавьте фото')
    bot.register_next_step_handler(msg, get_photo)
    isRunning = False


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """сохранение фотографий на диске в папке db_files/photos"""
    try:
        foto_id = bot.get_file(message.photo[-1].file_id)  # id фото с макс разрешением
        downloaded_file = bot.download_file(foto_id.file_path)  # загрузить в переменную файл фото с сервака телеги
        filename, file_extension = os.path.splitext(foto_id.file_path)
        src = "db_files/photos/" + str(message.from_user.id) + '_' + str(message.id) + file_extension
        print('src - ', src)
        with open(src, 'wb') as new_file:  # записываем в файл данные
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото сохранено успешно")
        print("Фото сохранено успешно")
    except Exception as e:  # исключение, если не удалось сохранить фотку
        print("Не удалось сохранить фото, ошибка в модуле get_photo: \n", e)
        bot.reply_to(message, f"Не удалось сохранить фото, ошибка в модуле get_photo: \n + {e}")


def db_add_text(msg_id: int, user_id: int, first_name: str, last_name: str, time, text: str):
    """добавление текста в бд"""
    cursor.execute('INSERT INTO text (msg_id, id_user, first_name, last_name, time, text) VALUES (?, ?, ?, ?, ?, ?)',
                   (msg_id, user_id, first_name, last_name, time, text))
    conn.commit()


def db_add_foto(msg_id, file_path):
    cursor.execute('UPDATE text SET file_path = ? WHERE msg_id = ?', (file_path, msg_id))
    conn.commit()


def db_show(user_id):
    """"вывод списка из базы данных"""
    qwerty = cursor.execute('SELECT * from text where id_user = ?', (user_id,))
    conn.commit()
    text_list = []
    for i in qwerty:
        print("ФИО пользователя:", i[3], " ", i[4])
        print("Время создания:", i[5])
        print("Текст:", i[6], end="\n\n")
        text_list.append(str(f'ФИО пользователя: {i[3]} {i[4]}\nВремя создания: {i[5]}\nТекст: {i[6]}\n\n'))
    text_list = ' '.join(text_list)
    return text_list


@bot.message_handler(commands=['show'])
def show(message):
    bot.send_message(message.chat.id,
                     f'Список задач пользователя: {message.from_user.first_name} {message.from_user.last_name}')
    sss = db_show(message.from_user.id)
    bot.send_message(message.chat.id, sss)


# функция пустышка, чтоб при форматировании кода в файле main.py не удалялся импорт
def deffdb():
    pass


def def_pass_from_db_database():
    """функция пустышка для главной страницы"""
    pass


'''

def read_sqlite_table(message):
    global sqlite_connection, qaz
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()
        # print("---------------------------------------")
        print("Подключен к SQLite")

        sqlite_select_query = "SELECT * from text"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        # print(records)
        qaz = []
        for row in records:
            # print("---------------------------------------")
            # print(row)
            print("ID_записи:", row[0])
            print("ID_user:", row[1])
            print("Текст:", row[2])
            print("Время добавления:", row[3], end="\n\n")
            # print("Зарплата:", row[4], end="\n\n")

            qaz.append(str(f'ID_записи: {row[0]}, ID_user: {row[1]}, Текст: {row[2]}, Время добавления: {row[3]} \n'))
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    bot.send_message(message.chat.id, ' '.join(qaz))



def db_add_text(user_id, nickname):
     cursor.execute("UPDATE `subscriptions` SET `nickname` = ? WHERE `user_id` = ?",
                               (nickname, user_id))



userr_id = message.from_user.id
userr_text = message.text
time_text = datetime.date.today().strftime("%Y-%m-%d")
mes = message
db_table_text(user_id=userr_id,
              user_text=userr_text,
              time=time_text,
              message=mes)


'''
