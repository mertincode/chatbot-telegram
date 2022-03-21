import telebot

token = '5238865528:AAGBDsgaZfUHnYOBQpvAnC7MhIhWyRgpIw0'

bot = telebot.TeleBot(token)

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types



# Заготовки для двух ситуаций
first = ["Кот, тобi пiзда!"]
second = ["Влад, тобi пiзда!"]

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(commands=['start'])
def start_message(message):
    # Ответ на запуск бота
    bot.send_message(message.from_user.id, "Привет, это тестовый чат-бот, который помогает Алексею выучить Python.")

    keyboard = types.InlineKeyboardMarkup()

    key_cat = types.InlineKeyboardButton(text='Кот насрал мимо лотка', callback_data='cat')
    keyboard.add(key_cat)

    key_vlad = types.InlineKeyboardButton(text='Влад обоссал стульчак', callback_data='vlad')
    keyboard.add(key_vlad)

    bot.send_message(message.from_user.id, text='Выбери жизненную ситуацию', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет!")

        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждой ситуации
        key_cat = types.InlineKeyboardButton(text='Кот насрал мимо лотка', callback_data='cat')

        # И добавляем кнопку на экран
        keyboard.add(key_cat)

        key_vlad = types.InlineKeyboardButton(text='Влад обоссал стульчак', callback_data='vlad')
        keyboard.add(key_vlad)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери жизненную ситуацию', reply_markup=keyboard)

        # Ответ на команду /help
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")

        # Ответ на любое другое сообщение
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    # Если нажали на кнопку про кота
    if call.data == "cat":
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, first)

    # Если нажали на кнопку про Влада
    if call.data == "vlad":
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, second)

bot.polling(none_stop=True)
