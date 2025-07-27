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

driver.get("http://uitestingplayground.com/ajax")
print("[Ресурс окрыт]")

obj_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
print("[Элемент 'Кнопка' найдена]")

obj_button.click()
print("[Произошло нажатие на кнопку]")
# на этом моменте возникает ошибка p.bg-success

obj_text_response = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"p.bg-success")))
print("[Элемент 'Зеленая плашка' найден]")

print("[Текст ответа]:", obj_text_response.text)

print("[Завершение скрипта]")
driver.quit()


#Другой ариант решения
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пример 1
# Ожидание загрузки кнопки
obj_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
obj_button.click()

# Ожидание появления текста
obj_text_response = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
print("Текст ответа:", obj_text_response.text)


"""