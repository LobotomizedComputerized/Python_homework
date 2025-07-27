

class Check_Info:

    def __init__(self_1, par_1):
        print("[Функция init - активирована]")
        self_1.per_driver = par_1

        #Операции с полем ввода FirstName
    def field_FirstName_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).send_keys("Test")
        print("[Элемент найден - поле ввода FirstName]")

    #Операции с полем ввода LastName
    def field_LastName_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).send_keys("Sample")
        print("[Элемент найден - поле ввода LastName]")

    def field_PostalCode_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).send_keys("1234576")
        print("[Элемент найден - поле ввода PostalCode]")

    #Операции с кнопкой Login
    def btn_checkout_operations(self_2,par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка Continue]")