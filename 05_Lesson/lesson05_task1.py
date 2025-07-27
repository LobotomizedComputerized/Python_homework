from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

print("[Активация программы]")
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")
print("[Открыт ресурс: http://uitestingplayground.com/classattr]")
sleep(5)

button_blue = driver.find_element(By.CSS_SELECTOR, "button.class2")
print("[Элемент найден]")
sleep(5)

button_blue.click()
print("[Произошло нажатие кнопки]")
sleep(5)
print("[Конец программы]")