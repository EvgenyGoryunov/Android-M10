from time import sleep

from telebot import types

from config import bot
from leisure_text import *


@bot.message_handler(commands=['leisure'])
def leisure(message):
    """формирование кнопок досуга"""
    buttons = ['Баня/сауна', 'На шашлыки', 'Кино', 'Ночной клуб', 'Кафе']
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button_list = [types.InlineKeyboardButton(text=x, callback_data=x) for x in buttons]
    keyboard.add(*button_list)
    bot.send_message(message.chat.id, text="Выберите куда хотите сходить", reply_markup=keyboard)


def form_list(listt):
    """формирование сообщения в правильном формате (нумерация + сообщение + команда)"""
    q, i = 0, 2
    global list_first, listt2, list_from, list_to, copy_list_first

    list_first = listt
    listt2 = [''] * len(list_first)
    while q < len(listt):
        # заменяем ** на пустоту, убираем в конце слов звездочки
        if listt[q][-2:] == '**' or listt[q][-3:] == '** ' or listt[q][-4:] == '**  ':
            listt[q] = f"{listt[q].replace('**', '')}"
            q += 1
        # заменяем * на пустоту
        elif listt[q][-1] == '*' or listt[q][-2] == '*' or listt[q][-3] == '*':
            listt[q] = f"\n\n{listt[q].replace('*', '')}"
            # добавляем в список listt2 подзаголовки блоково сообщений
            listt2[q] = listt[q]
            q += 1
        else:
            listt[q] = f'\n· {i - 1}. {listt[q]}   /add{i - 1} '
            q += 1
            i += 1

    listt2[-1] = '\n\n ------------ЧТО ОСТАЛОСЬ----------------'
    listt2[0] = '\n\n ----------------ЧТО ВЗЯТО--------------------'
    copy_list_first = list_first.copy()
    list_from = []
    list_to = []


def send_mes_sov(listt, message):
    """форматирование списка советов нужного формата"""
    q, i = 0, 2
    while q < len(listt):
        if listt[q][-2:] == '**' or listt[q][-3:] == '** ' or listt[q][-4:] == '**  ':
            listt[q] = f"{listt[q].replace('**', '')}\n"
            q += 1
        else:
            listt[q] = f'\n➤ {i - 1}. {listt[q]}'
            q += 1
            i += 1
    return bot.send_message(message.chat.id, ' '.join(listt))


@bot.message_handler(commands=['banysovet'])
def banysovet(message):
    listt = message_bany_sovet.copy()
    send_mes_sov(listt, message)


@bot.message_handler(commands=['shashliksovet'])
def shashliksovet(message):
    listt = massage_bany_shashlik.copy()
    send_mes_sov(listt, message)


def send_message(listt, call):
    """отправка сообещения пользователю"""
    return bot.send_message(call.message.chat.id, ' '.join(listt))


@bot.callback_query_handler(func=lambda call: True)
def main_leisure(call):
    """"реакция на команды на клавиатуру под сообщением"""
    # bot.answer_callback_query(callback_query_id=call.id, text='Отлично!')

    if call.data == 'Баня/сауна':

        messages = massage_bany.copy()
        form_list(messages)
        send_message(messages, call)

    elif call.data == 'На шашлыки':
        messages = messages_shashlik.copy()
        form_list(messages)
        send_message(messages, call)


list_add = []
for i in list(range(30)):
    """формирует список команд add1, del1, add2, del2 и тд"""
    list_add.append(f'add{i + 1}')
    list_add.append(f'del{i + 1}')


@bot.message_handler(commands=list_add)
def adds(message):
    """удаление из первого списка элемента и добавление в второй и обратно из 2 в 1"""
    # print('-------------------')
    # print(message.text)
    # print('до: ', message.text)

    # проверка входной команды (add/del)
    viewList_first = True

    if message.text.find('add') != -1:
        # print('после: ', message.text)
        indexAdd = 0
        # форм поискового запроса (add1 ) - пробел в конце обязательно
        foundStr = f'{message.text} '

        if not len(list_first):
            bot.send_message(message.chat.id, '❗ Позиция уже добавлена в список ❗')

        for strTextAdd in list_first:

            if strTextAdd.find(foundStr) == -1 and indexAdd < len(list_first) - 1:
                indexAdd += 1

            # значит, что нашел совпадение
            elif strTextAdd.find(foundStr) != -1:
                list_first[indexAdd] = ''
                list_from.clear()
                list_to.clear()

                # проверка на завершение списка "что осталось" и выполнение условий
                qwe = 1
                for iq in list_first:
                    if iq.find('add') != -1:
                        qwe += 1
                        break
                    if qwe == len(list_first):
                        qwe += 1
                        listt2[0] = '\n\n ---------------ВЫПОЛНЕНО--------------'
                        listt2[-1] = '\n\n --------------------------------------------------'

                        viewList_first = False

                        break
                    else:
                        qwe += 1

                listt2[indexAdd] = strTextAdd

                # форм списка 'что уже взято' (верхний) list_to на основе списка listt2
                for i in listt2:
                    # формир список из добавленных элементов
                    if i != '':
                        # меняем команду в конце сообщения add на del
                        i = i.replace('add', 'del')
                        list_to.append(i)
                bot.send_message(message.chat.id, ' '.join(list_to))

                # форм списка 'что осталось' (нижний) list_from на основе списка list_first
                if viewList_first == True:
                    # формир список из оставшихся элементов
                    for i in list_first:
                        if i != '':
                            list_from.append(i)
                    bot.send_message(message.chat.id, ' '.join(list_from))
                break

            else:
                bot.send_message(message.chat.id, '❗ Позиция уже добавлена в список ❗')
                break

    if message.text.find('del') != -1:

        indexDel = 0
        foundStr = f'{message.text} '
        foundStrListFirst = foundStr.replace('del', 'add')

        for strTextDel in copy_list_first:
            if strTextDel.find(foundStrListFirst) == -1:
                indexDel += 1
            elif strTextDel.find(foundStrListFirst) != -1:
                list_first[indexDel] = copy_list_first[indexDel]
                listt2[indexDel] = ''
                break

        list_from.clear()
        list_to.clear()

        viewList_listt2 = False
        for iq in listt2:

            if iq.find('add') != -1:
                viewList_listt2 = True
                break

        if viewList_listt2 == True:
            for i in listt2:
                if i != '':
                    i = i.replace('add', 'del')
                    list_to.append(i)
            bot.send_message(message.chat.id, ' '.join(list_to))

        if len(list_first):
            for i in list_first:
                if i != '':
                    list_from.append(i)
            bot.send_message(message.chat.id, ' '.join(list_from))


""""""


# функция пустышка, чтоб при форматировании кода в файле main.py не удалялся импорт
def deffrem():
    sleep(0.001)
    pass


def def_pass_from_db_leisure():
    """функция пустышка для главной страницы"""
    pass

'''
                    # print("U+267F", ord('♿'))
                    
такой сценарий, например маме нужно купить лекарства, она пишет или фото присылает, и ставит задачу
чтоб я купли, выбирает вариант аптека, и когда я начинают ехать, или выхожу из дома
например в нужное время, не ночью, а когда обычно аптеки работают, появляет сообщение, что моно купить 
по пути лекарства для родителей, и сразу создать сценарий, сближения, что если мама поедет ко мне
либо я к ним, либо задать локацию нахождения лекарсва, и когда мама например будет у меня дома, сообщение появится
чтоможно забрать лекарство

спросить у кого нибудь, когда вы выбираете или передать друг другу, сближение двух человек реагирует
например я хотел у брата кое что  спросить, и когда система распознала, что мы находимся в одной точке, появляется
сообщение, что вы хотели сообщить то-то или то-то


когда срабатывает напоминалка, она сообщает что пора и предоставляет список того, что нужно взять
типа не желаете проверить свою собранность к делам


для автоледи, как заменить колесо
как поеменять колеса

для автомужиков
бросить клич о помощи, для всех подписчиков в данном городе

для гаи, как вести себя с гваишником
как оспорить прямо на ходу его замечание


функция поискап детей
зарядить телефон по макс, если есть чехол влагозащитный, поместите в него
если плохая связь, то пишет лог на сервер и в телефон, последние координаты, если садится телефо
также пишет координаты, также сообщает родителям, что телефон разряжен, послдение координыты 
задержка на выключение, включание дистанционно геолокации иэнегросбережения на телефоне ребенка



поход в лес справка, как себя вести в случае если вы заблудились

первая медицинская помощь

для мужчин
пикам методы
в каких клубах какие девчонки водятся, контенген
номера проституток и для мужчин

телеграмм бот для детей
пишит лог координат, чтоб если потеряется, можно опередлить последнее местоположение ребенка, либо если куда нибудь
зашел из зоны окределенной, напрмиер школу покинул и ушел не туда, куда нужно

рецепты для шашлыков хорошие и простые, как папа делает

внизу сделать после советов возможность добавить свое свои пункты и свой список

сделать заголовки в виде двух звездочек в конце ** - самый большой уровень, * уровено по меньше

отдых для одного, для друг + друг, для парень - девушка, для муж - жена, для семьи, куда сводить детей
компанией
с детьми - раскраска себя и всех, анимация

для одного - поплавать, поиграть в футбол, поухаживать за животными

бот который помогает лениться

фабрика добрых дел: купить в питомник еды, принять участие в посадке деревьев, уборке улиц на суботнике

где заказать вкусный шашлык (шашлыков + соусы) + цена

контактный зоопарк
покататься на лошадях
я строитель
забор - как правильно сделать

пикап лдя мужчин, максимально упростить

экстрим
прыжок с парашута, тарзанки, ныряние с акваланга, катание на горках, на бубликах, катание летом на бублике и батуте
катание на

активный отдых
караоке, танцы, катание на лыжах, коньках, виртуальная реальность, прогулка, игры в квесты, на

катание на мототехнике
на снегоходе, на квадроциклах, на картинги, на обычных мотоциклах

пассив
кафе, в гор сад атракционы, кино, кино5д, рисование, лепка из глины, часы сделать, фотосессия

'''
