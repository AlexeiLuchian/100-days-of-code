from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

elements_name = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last > div > ul > li > a")
elements_time = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last > div > ul > li > time")

events_dict = {i:{'name': elements_name[i].text, 'time' : elements_time[i].text} for i in range(len(elements_name))}
print(events_dict)

driver.quit()