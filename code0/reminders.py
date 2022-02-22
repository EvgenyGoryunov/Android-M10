import datetime
import time

import schedule

from config import bot

time_start = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def job():
    print(f"Планировщик задач запущен:\n{time_start}")
    bot.send_message('1328091869', f"Планировщик задач запущен:\n{time_start}")


def start_schedule():
    """расписание запусков задач (функций)"""
    # schedule.every(15).seconds.do(job)

    while True:
        schedule.run_pending()  # для подгрузки новых задач
        time.sleep(10)  # проверяет каждые __ секунд


def def_pass_from_db_reminders():
    """функция пустышка для главной страницы"""
    pass


"""******************************************* ПОЛЕЗНЫЕ ССЫЛКИ *****************************************************"""

"""
по schedule
https://russianblogs.com/article/21691175263/

по формате даты
https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/
https://www.defpython.ru/kak_v_python_poluczit_tekusczuu_datu_i_vremya

def job():
    print("I'm working...")
    # Run job every 3 second/minute/hour/day/week,
    # Starting 3 second/minute/hour/day/week from now
    schedule.every(3).seconds.do(job)
    schedule.every(3).minutes.do(job)
    schedule.every(3).hours.do(job)
    schedule.every(3).days.do(job)
    schedule.every(3).weeks.do(job)
    # Run job every minute at the 23rd second
    schedule.every().minute.at(":23").do(job)
    # Run job every hour at the 42rd minute
    schedule.every().hour.at(":42").do(job)
    # Run jobs every 5th hour, 20 minutes and 30 seconds in.
    # If current time is 02:00, first execution is at 06:20:30
    schedule.every(5).hours.at("20:30").do(job)
    # Run job every day at specific HH:MM and next HH:MM:SS
    schedule.every().day.at("10:30").do(job)
    schedule.every().day.at("10:30:42").do(job)
    # Run job on a specific day of the week
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().minute.at(":17").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
"""
