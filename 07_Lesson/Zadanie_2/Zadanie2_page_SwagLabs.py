
class page_SwagLabs:
    #Инициализация драйвера
    def __init__(self_1, par_1):
        print("[Функция init - активирована]")
        #Инициализация драйвера
        self_1.per_driver = par_1
        #Отключение ненужных служб
        self_1.per_driver.execute_script("window.alert = function() {}; window.confirm = function() { return true; }")
        

    def find_btn_add1(self_2, par_1, par_2):
        self_2.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка Add to cart]")


    def find_btn_add2(self_3, par_1, par_2):
        self_3.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка Add to cart]")
        

    def find_btn_add3(self_4, par_1, par_2):
        self_4.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка Add to cart]")
        

    def find_btn_cart(self_4, par_1, par_2):
        self_4.per_driver.find_element(par_1, par_2).click()
        print("[Элемент найден - кнопка для перехода в корзину]")


