# Импортирование библиотек.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # автоматическое нажиматие на ссылки.
import time


class Main(object):
    def __init__(self, name=None):  # Конструктор __init__ инициализирует вебдрайвер, принимает параметр name (Ввод пользователя в телеграмм чате).
        self.driver = webdriver.Chrome()
        self.name = name

    def parse(self):
        res = self.go_to_page()
        return res

    def go_to_page(self):
        self.driver.get('https://twitter.com/explore')
        time.sleep(4)
        search = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div[2]/div[1]/div/div/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')  # Определение окно поиска

        str_name = str(self.name)
        # mess = str_name + ' Twitter'
        search.send_keys(str_name)
        search.send_keys(Keys.ENTER)  # Процесс ввода в поисковую строку и запуск поиска

        time.sleep(4)
        self.driver.find_element_by_partial_link_text("Люди").click()
        # Переход по первой ссылке
        #  //*[@id="react-root"]/div/div/div[2]/header/div[2]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/span
        time.sleep(4)  # Ждем пока страница загрузится

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/section/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span').click()
        time.sleep(4)
        list = []  # В этот список собирается ответ для возвращения в модуль main_script.py

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

        tri_inf_true = 'Крайнее сообщение,опубликованное в социальной сети Twitter ' + four_inf.text + ' назад - "' + tri_inf.text + '"'  # Добавляю в список последний опубликованный твит и время публикации

        list.append(first_inf_true)
        list.append(sec_inf_true)
        list.append(tri_inf_true)

        return list  # Возвращаю полученный результат в виде списка

        # time.sleep(50)
        # self.driver.close()
        # elements = self.driver.find_elements_by_tag_name('a')
        # for i in elements:
        # print(i.get_attribute('href'))


def main(atr):
    answer = Main(atr)
    result = answer.parse()
    for i in result:
        print (i)

    # btn = driver.find_element_by_class_name("details")


if __name__ == '__main__':
    user_input = input("Введите посиковой запрос: \n")
    main(user_input)
# В случае импорта модуля, код не запускается на выполнение.
