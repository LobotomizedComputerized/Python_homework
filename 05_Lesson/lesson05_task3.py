from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/inputs")
print("[Открыт ресурс: https://the-internet.herokuapp.com/inputs]")
sleep(3)

find_inp = driver.find_element(By.TAG_NAME, "input")
print("[Элемент найден]")
sleep(3)

find_inp.send_keys("Sky")
print("[Текст 'Sky' введен ]")
sleep(3)

find_inp.clear()
print("[Поле вода очищено]")
sleep(3)

find_inp.send_keys("Pro")
print("[Текст 'Pro' введен ]")
sleep(3)

driver.quit()
print("[Конец программы]")