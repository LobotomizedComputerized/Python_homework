
"""
        #Нахождение объекта "Окно с результатом" по локатору 'div[class="screen"]'
       
obj_screen = WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15")
)
print("[Элемент найден - поле отображения результата]")
sleep(3)

            #Извлечение текста из элемента "Окно с результатом" по локатору 'div[class="screen"]'
obj_screen_text = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="screen"]'))).text
print("[Элемент найден успешно - поле отображения результата]")
sleep(3)
        #Применение метода assert - проверка результа извлеченного из локатора с ожидаемым результатом "15"

#Тестовый скрипт

print(obj_screen_text, type(obj_screen))


print("[Начало проверки]")
assert int(obj_screen_text) == 15
print("[Конец проверки]")
sleep(3)

(WebDriverWait, EC.presence_of_element_located, By.CSS_SELECTOR, 'div[class="screen"]')

"""


class main_page:
        # Базовые операции для начала работы с драйвером
#____Настройка_рабочей_среды_____

    def __init__(func1_self, driver):  
        print("[Открытие ресурса]")
        func1_self.per_driver = driver
        func1_self.per_driver.implicitly_wait(10)
        func1_self.per_driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#____________________________________

#____Операции с полем ввода____________
    def field_operations(func2_self, par1, par2):
        print("[Функция field_operations - активирована]")

        #Нахождение поля по атрибуту id #delay локатора и очистка
        func2_self.field = func2_self.per_driver.find_element(par1, par2)
        print("[Элемент найден  - Поле ввода]")

        #Очистка поля ввода от символов
        func2_self.field.clear()
        print("[Очистка поля ввода произведена успешно]")

        #Ввод новых значений в поле ввода
        func2_self.field.send_keys("45")
        print("[Ввод символов в поле ввода осуществленно успешно]")
#_____________________________________



#____Действия скнопками калькулятора_____
        #Операции с кнопкой 7
            #Нахождение кнопки
    def btn1_num_7(func3_self, par1, par2):
        print("[Функция btn1_num_7 - активирована]")
        func3_self.per_driver.find_element(par1, par2).click()
        print("[Элемент найден - кнопка 7]")

        #Операции с кнопкой +
            #Нахождение кнопки 
    def btn2_oper_sum(func3_self, par1, par2):
        print("[Функция btn2_oper_sum - активирована]")
        func3_self.per_driver.find_element(par1, par2).click()
        print("[Элемент найден - кнопка +]")

        #Операции с кнопкой 8
            #Нахождение кнопки
    def btn3_num_8(func3_self, par1, par2):
        print("[Функция btn3_num_8 - активирована]")
        func3_self.per_driver.find_element(par1, par2).click()
        print("[Элемент найден - кнопка 8]")


        #Операции с кнопкой =
            #Нахождение кнопки
    def btn4_oper_equal(func3_self, par1, par2):
        print("[Функция btn4_oper_equal - активирована]")
        func3_self.per_driver.find_element(par1, par2).click()
        print("[Элемент найден - кнопка =]")
#___________________________________________

#__________Действия_окном_для_отображения_результата__________

            #Скрипт на поиск элемента - поле результата
    def find_field_resault(func4_self, web_wait_1, par_2, par_3):
        #Нахождение объекта "Окно с результатом" по локатору 'div[class="screen"]'
        web_wait_1(func4_self.per_driver, 50).until(par_2)
        print("[Нахождение объекта - окно с результатом, ожидание обновление текста]")

        func4_self.obj_screen_text = web_wait_1(func4_self.per_driver, 50).until(par_3).text
        print("[Объект найден - окно с результатом и извлечение текста в переменную]")

        return func4_self.obj_screen_text
#______________________________________________________________