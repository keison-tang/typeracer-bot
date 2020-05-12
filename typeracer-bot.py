from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from utils.input import inputWPM
from utils.characters import wordCount, charCount
from utils.delay import timeDelay

import time

wpm = inputWPM()

driver = webdriver.Chrome()
driver.get('https://play.typeracer.com/?universe=insane')

assert "TypeRacer" in driver.title

wait = WebDriverWait(driver, 10)

practice = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')))
practice.click()

html = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inputPanel')))
excerpt = html.find_element_by_css_selector('tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div')

print("Text: " + excerpt.text)
print("Words: " + str(wordCount(excerpt.text)))
print("Chars: " + str(charCount(excerpt.text)))

delay = timeDelay(wpm, wordCount(excerpt.text), charCount(excerpt.text))
print(delay)

textInput = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')))

for word in excerpt.text:
    textInput.send_keys(word)

    if word == " ":
        time.sleep(delay)
