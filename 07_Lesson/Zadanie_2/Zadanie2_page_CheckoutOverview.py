import re


class CheckoutOverview:
    #инициализация драйвера
    def __init__(self_1, par_1):
        print("[Функция init - активирована]")
        self_1.per_driver = par_1

    def find_text_reasault(self_2, web_d_wait_1, ec_presence_of_element_2):
        self_2.text = web_d_wait_1(self_2.per_driver, 20).until(ec_presence_of_element_2).text
        print("[Элемент найден - текст с результатом]")

        #Скрипт ломается на этом моменте, почему?
        test = re.search(r"\d+\.\d+", self_2.text)
        print("[Проверка на наличие числа - 58.29]")
        number = float(test.group())
        #____________________________________
        return number

