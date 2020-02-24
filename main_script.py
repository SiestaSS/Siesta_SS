import telebot  # Основной модуль для взаимодействия с телеграмм.
from telebot.types import Message
import config  # Модуль с токеном бота.
import script_for_twitter  # Модуль выполняет задачу по сбору информации из Twitter.

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])  # Декоратор обрабатывает запрос(команду) от пользователя /start
def start(message):
    sent = bot.send_message(message.chat.id, 'Как Вас зовут?')

    def hello(message):  # Генерация ответа на команду от пользователя.
        bot.send_message(message.chat.id,
                         'Добрый день {name}. Моей задачей является поиск информативных признаков подготовки к проведению "цветных революций". '.format(
                             name=message.text))
        bot.send_message(message.chat.id,
                         'Я произвожу анализ информации в социальной сети Twitter, у пользователей, выступающих в качестве легитимизаторов революционных действий')
        bot.send_message(message.chat.id,
                         '{name}, просто отправьте мне фамилию пользователя или название оппозиционной партии..'.format(
                             name=message.text))

    bot.register_next_step_handler(sent, hello)


@bot.message_handler(content_types=['text'])  # Декоратор обрабатывает сообщения от пользователя.
def hen_message(message: Message):
    usr_mess = str(message.text)  # Переменная хранит запрос от пользователя.

    answer = script_for_twitter.Main(usr_mess)  # Создане обьекта класса Main. Конструктор обрабатывает переданный аргумент.
    ans = answer.make_logfile()  # Возвращает список, отправка ответа пользователя реализована через цикл.
    for i in ans:
        bot.send_message(message.chat.id, i)


bot.polling(none_stop=True)
