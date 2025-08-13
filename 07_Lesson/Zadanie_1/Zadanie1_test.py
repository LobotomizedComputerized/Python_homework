#Необходимые инструменты
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#Импорт класса из модуля Zadanie1_MainPage
from Zadanie1_MainPage import main_page


def test_func():
#____Настройка_рабочей_среды_________
    #Инициализация драйвера
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #Создание объекта и импортирование переменной browser как аргумент функции init в модуле main_page
    test_obj = main_page(browser)
#____________________________________


#____Операции_с_полем_ввода__________
    # Вызов функции field operation и ввод позиционного аргумента By.CSS_SELECTOR, 'input[id="delay"]'
    test_obj.field_operations(By.CSS_SELECTOR, 'input[id="delay"]')
#____________________________________


#____Действия_скнопками_калькулятора_____
    #Нахождение кнопки 7 и нажатие на нее
    test_obj.btn1_num_7(By.XPATH, '//span[text()="7"]')

    #Нахождение кнопки + и нажатие на нее
    test_obj.btn2_oper_sum(By.XPATH, '//span[text()="+"]')

    #Нахождение кнопки 8 и нажатие на нее
    test_obj.btn3_num_8(By.XPATH, '//span[text()="8"]')

    #Нахождение кнопки = и нажатие на нее
    test_obj.btn4_oper_equal(By.XPATH, '//span[text()="="]')
#_______________________________________


#__________Действия_окном_для_отображения_результата________
    #Скрипт на поиск элемента - поле результата - эксперимент
    test_of_screen_resault = test_obj.find_field_resault(
        WebDriverWait, 
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"),
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="screen"]'))
        )

    #Проверка того что результат в окне соответствует числу 15
    assert int(test_of_screen_resault) == 15
    print("[Текст из окна с результатом в калькуляторе соответствует числу 15]")

#___________________________________________________________

#__________Закрытие браузера_________
    print("[Закрытие браузера]")
    browser.quit()
#____________________________________

