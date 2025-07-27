
class main_page:

#____Этот участок кода работает!_____

    #Создание функции конструктора для начала работы
    def __init__(self_1, par_1):
        print("[Функция init - активирована]")

        #Инициализация драйвера
        self_1.per_driver = par_1

        #Отключение ненужных служб
        self_1.per_driver.execute_script("window.alert = function() {}; window.confirm = function() { return true; }")

        #Создание неявного ожидания
        self_1.per_driver.implicitly_wait(10)

        #Открытие ресурса
        self_1.per_driver.get("https://www.saucedemo.com")
        print("[Открытие ресурса]")

        #Очистка куки
        self_1.per_driver.delete_all_cookies()
        print("[Удаление всех куки]")

#______________________________________


#____Этот участок кода работает!_____
    #Операции с полем ввода Username
    def field_Username_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).send_keys("standard_user")
        print("[Элемент найден - поле ввода Username]")

    #Операции с полем ввода Password
    def field_Password_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).send_keys("secret_sauce")
        print("[Элемент найден - поле ввода Password]")

    #Операции с кнопкой Login
    def btn_login_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка Login]")

#______________________________________








