from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

            #РЕШЕНИЕ 1
"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
print("[Ресурс открыт]")

#img[src="img/award.png"]
obj_img = driver.find_element(By.CSS_SELECTOR,'img[src="img/award.png"]')
print("[Элемент найден]")

obj_img.get_attribute("src")
print("[Атрибут найден успешно]")

driver.quit()
print("[Заверешение скрипта]")
"""
            #РЕШЕНИЕ 2
"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
print("[Ресурс открыт]")
sleep(3)

#img[src="img/award.png"]
obj_img = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="img/award.png"]')))
print("[Элемент найден]")
sleep(3)

obj_img.get_attribute("src")
print("[Атрибут найден успешно]")
sleep(3)

driver.quit()
print("[Заверешение скрипта]")
"""

            #ДРУГОЙ ВАРИАНТ РЕШЕНИЯ
"""
try:
    # Переход на страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    
    # Ожидание загрузки текста "Done"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done")
    )

    # Получение src атрибута третьей картинки
    third_image = driver.find_elements(By.TAG_NAME, "img")[2]
    src_value = third_image.get_attribute("src")
    print("Значение атрибута src у 3-й картинки:", src_value)

finally:
    # Закрытие браузера
    driver.quit()
"""