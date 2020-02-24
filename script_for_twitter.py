# Импортирование библиотек.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # автоматическое нажиматие на ссылки.
import time
import logging #Модуль для создания .log файла
"""logger обрабатывает сообщения уровня DEBUG
   сообщения от других обработчиков игнорируются т.к. присвоен уровень CRITICAL """
logging.basicConfig(level='DEBUG',filename='mylog.log')
logger = logging.getLogger()
logging.getLogger('urllib3').setLevel('CRITICAL')
logging.getLogger('selenium').setLevel('CRITICAL')
logging.getLogger('requests').setLevel('CRITICAL')

class Main(object):
    def __init__(self, name=None):  # Конструктор __init__ инициализирует вебдрайвер, принимает параметр name (Ввод пользователя в телеграмм чате).
        self.driver = webdriver.Chrome()
        self.name = name

    def make_logfile(self):
        """Процесс формирования сообщения и запись в log файл"""
        logger.debug( 'Дата и время отправки сообщения:'+time.strftime('%d %m %Y  %H %M') + '\n'+ f'The message from user: {self.name}')
        """получение результата с соц. сети Twitter"""
        res = self.go_to_page()
        logger.debug('The result from method "Main.go_to_page()" was correct. ')
        logger.debug(f'The result is: {res} ')
        return res

    def go_to_page(self):
        self.driver.get('https://twitter.com/explore') #переход на сайт twitter
        time.sleep(4)

        search = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div[2]/div[1]/div/div/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')  # Определение окно поиска
        str_name = str(self.name)
        search.send_keys(str_name)
        search.send_keys(Keys.ENTER)  # Процесс ввода в поисковую строку и запуск поиска
        time.sleep(4)
        try:
            self.driver.find_element_by_partial_link_text("Люди").click() #Переход на вкладку люди
            time.sleep(4)  # Ждем пока страница загрузится
        except:
            self.driver.find_element_by_partial_link_text("People").click()  # Переход на вкладку люди
            time.sleep(4)  # Ждем пока страница загрузится

        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span').click()
            time.sleep(4)
            list = []  # В этот список собирается ответ для возвращения в модуль main_script.py или для вывода в терминал

            """Сбор информации осуществляется по XPath """
            first_inf = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/span')
            first_inf_true = 'Информация из социальной сети Twitter ' + first_inf.text  # Общая информация о найденном ресурсе.

            sec_inf = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
            sec_inf_true = sec_inf.text + ' пользователей сети подвержено влиянию'  # Определение количества людей

            tri_inf = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[2]/span')

            four_inf = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[1]/div/div[1]/a/time')

            tri_inf_true = 'Крайнее сообщение,опубликованное в социальной сети Twitter ' + four_inf.text + ' назад - "' + tri_inf.text + '" \n'  # Добавляю в список последний опубликованный твит и время публикации

            list.append(first_inf_true)
            list.append(sec_inf_true)
            list.append(tri_inf_true)

            return list  # Возвращаю полученный результат в виде списка
        except:
            list = ['Не удалось найти информацию по вашему запросу \n']
            return list


def main(atr):
    answer = Main(atr)
    result = answer.make_logfile()
    for i in result:
        print (i)



if __name__ == '__main__': # В случае импорта модуля, код ниже не запускается на выполнение.
    print(
        'Добрый день. Моей задачей является поиск информативных признаков подготовки к проведению "цветных революций"  \n'
        'Я произвожу анализ информации в социальной сети Twitter, у пользователей, выступающих в качестве легитимизаторов революционных действий \n'
        'Просто отправьте мне фамилию пользователя или название оппозиционной партии.. \n')

    print('Для завершения работы программы, напишите --> stop  \n')
    while True:
        user_input = input("Введите поисковой запрос: ")
        if user_input == "stop":
            break
        else:
            main(user_input)
