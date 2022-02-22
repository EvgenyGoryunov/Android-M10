import datetime
import time
from multiprocessing import Process

import db_script
import handlers
import leisure
import reminders
from config import bot
from database import def_pass_from_db_database

time_start = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def start_bot():
    print('Bot start', time_start, end='\n')
    bot.polling(none_stop=True)


def start_reminders():
    reminders.start_schedule()


if __name__ == '__main__':
    """для бесконечного перезапуска бота и планировщика"""
    """Process(target=... нужен для запуска одновременно двух функций"""
    p1 = Process(target=start_bot)
    p2 = Process(target=start_reminders)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

"""функция пустышка для главной страницы, чтоб при формате не удалялись импорты"""
db_script.def_pass_from_db_scripts()
reminders.def_pass_from_db_reminders()
handlers.def_pass_from_db_handlers()
leisure.def_pass_from_db_leisure()
def_pass_from_db_database()

"""*************************************** ВРЕМЕННО НЕ ЗАДЕЙСТВОВАН ***********************************************"""


def bot_start():
    """перезапуск бота иной метод, если бот выпадает"""
    while True:
        try:
            print("бот запущен в", time_start)
            reminders.start_schedule()
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print("произошла ошибка: ", e)
            print("бот перезапущен в", time_start)


"""******************************************* ПОЛЕЗНЫЕ ССЫЛКИ *****************************************************"""
""" 

видео по распараллеливанию процессов
https://www.youtube.com/watch?v=CNF_Z9-htlI&t=158

как разместить бота на сервер яндекса (до 100 000 запросов в месяц)
https://habr.com/ru/post/550456/

"""

# from config import bot
# from database import *
# from db_script import *
# from handlers import *
# from leisure import *
# from reminders import *
