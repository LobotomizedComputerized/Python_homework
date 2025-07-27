

class page_YourCart:

    def __init__(self_1, par_1):
        print("[Функция init - активирована]")
        self_1.per_driver = par_1

    def find_btn_checkout(self_2, par_1, par2):
        self_2.per_driver.find_element(par_1, par2).click()
        print("[Элемент найден - кгопка checkout]")
        pass

