# from main import bot
#
#
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет!')
#         print("проверка text - привет")
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Пока!')
#         print("проверка text - пока")
#     elif message.text.lower() == 'тест':
#         bot.send_message(message.chat.id, 'Тест!')
#         print("проверка text - тест")
#     # elif message.text.lower() == '🎲 рандом':
#     #     bot.send_message(message.chat.id, 'Рандомное число:  ' + str(random.randint(0, 100)))
#     #     print("проверка text - Рандомное число")
#     else:
#         bot.send_message(message.chat.id, 'Текст не распознан!')