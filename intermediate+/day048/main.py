from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://ozh.github.io/cookieclicker/")

language_btn = driver.find_element(By.CSS_SELECTOR, 'div.langSelectButton')
language_btn.click()

cookie_btn = driver.find_element(By.ID, "bigCookie")
products_btns = driver.find_elements(By.CSS_SELECTOR, 'div.product')

game_time = time.time() + 5 * 60
end_time = time.time() + 5
while time.time() < game_time:
    cookie_btn.click()
    if time.time() > end_time:
        for i in range(len(products_btns) -1, -1, -1):
            if products_btns[i].is_displayed() and products_btns[i].is_enabled():
                products_btns[i].click()
        end_time = time.time() + 5

cps_box = driver.find_element(By.ID, 'cookiesPerSecond')
cps_box_text = cps_box.text

driver.quit()
print(cps_box_text)