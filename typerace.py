import selenium
import time
import pyautogui
from selenium import webdriver


driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://play.typeracer.com/")

time.sleep(5)
pyautogui.hotkey("ctrl", "alt", "o")
time.sleep(5)

text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
print(type(text))
print(text[-1])
pyautogui.typewrite(text[-3], interval=0.001)
time.sleep(15)
driver.quit()
