#Необходимые инструменты
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#Импорт модулей для работы
from Zadanie2_main_page import main_page
from Zadanie2_page_SwagLabs import page_SwagLabs
from Zadanie2_page_Cart import page_YourCart
from Zadanie2_page_CheckInfo import Check_Info
from Zadanie2_page_CheckoutOverview import CheckoutOverview

#______________________Начало_скрипта__________________________
def test_func1():
    #Создание переменной browser для использования как аргумент, в которой происходит инициализация драйвера
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.execute_script("window.alert = function() {}; window.confirm = function() { return true; }")
    
#____main_page_____[Работает]
    #Создание объекта b импортирование аргумента browser
    test_obj = main_page(browser)

    #Операции с полем ввода Username
    test_obj.field_Username_operations(By.CSS_SELECTOR, 'input[placeholder="Username"]')

    #Операции с полем ввода Password
    test_obj.field_Password_operations(By.CSS_SELECTOR, 'input[placeholder="Password"]')

    #Операции с кнопкой Login
    test_obj.btn_login_operations(By.CSS_SELECTOR, 'input[data-test="login-button"]')  
#______________________________________



#____main_page_____[Работает]
    #Создание объекта и импортирование аргумента browser
    test_obj2 = page_SwagLabs(browser)

    #Кнопка Add to cart - #1
    test_obj2.find_btn_add1(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    sleep(5)

    #Кнопка Add to cart - #2
    test_obj2.find_btn_add2(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

    #Кнопка Add to cart - #3
    test_obj2.find_btn_add3(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-onesie"]')

    #Кнопка для перехода на страницу корзины
    test_obj2.find_btn_cart(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
#______________________________________



#____page_YorCart_____[Работает]
    test_obj3 = page_YourCart(browser)
    #Кнопка checkout
    test_obj3.find_btn_checkout(By.CSS_SELECTOR, 'button[id="checkout"]')
#______________________________________



#____Check_Your_Info_____[Работает]

    test_obj4 = Check_Info(browser)
    #Поле ввода First Name
    test_obj4.field_FirstName_operations(By.CSS_SELECTOR, 'input[placeholder="First Name"]')

    #Поле ввода Last Name
    test_obj4.field_LastName_operations(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')

    #Поле ввода Zip/Postal Code
    test_obj4.field_PostalCode_operations(By.CSS_SELECTOR, 'input[placeholder="Zip/Postal Code"]')

    #Кнопка continue
    test_obj4.btn_checkout_operations(By.CSS_SELECTOR, 'input[id="continue"]')

#______________________________________



#____Checkout_Overview_____[В разработке]

    #Создание объекта на сонове классаCheckout_Overview
    test_obj5 = CheckoutOverview(browser)

    #Объявление функции по нахождению элемента и извлечению из него текста
    text_for_test = test_obj5.find_text_reasault(WebDriverWait, EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]')))


    #Проверка того что текст содержит число 58.29
    assert text_for_test == 58.29
    print("[Текст из окна с результатом в калькуляторе соответствует числу 15]")
#______________________________________

    print("[Завершение скрипта]")
    sleep(3)
    browser.quit()
#__________Конец_скрипта__________________________

test_func1()
