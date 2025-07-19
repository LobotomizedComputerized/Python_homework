from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

print("[Начало скрипта]")

driver.get("http://uitestingplayground.com/textinput")
print("[Открытие ресурса]")

# локатор элемента input.form-control
inp_form_control = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control")))
print("[Элемент 'Поисковая строка' найдена]")

inp_form_control.send_keys("SkyPro")
print("[Текст в поисковую строку введен успешно]")

# локатор элемента button.btn.btn-primary
obj_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
print("[Элемент найден]")

obj_button.click()
print("[Нажатие на кнопку]")

# локатор элемента button.btn.btn-primary
obj_button2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
print("[Элемент найден]")

print("[Текст кнопки]:", obj_button2.text)

print("[Завершение скрипта]")
driver.quit()

# Другое решение задачи
"""
# Пример 2
# Ожидание загрузки поля ввода
inp_form_control = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control"))
)
inp_form_control.send_keys("SkyPro")

# Ожидание загрузки кнопки
obj_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
obj_button.click()

# Ожидание изменения текста кнопки
obj_button2 = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button.btn.btn-primary"), "SkyPro")
)
print("Текст кнопки:", obj_button2.text)

"""