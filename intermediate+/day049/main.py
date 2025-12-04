from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

ACCOUNT_EMAIL = "alexeiluchian@test.com"
ACCOUNT_PASSWORD = "sn4ckandl1ft"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
user_data_dir = os.path.join(os.getcwd(), 'chrome_profile')
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get(GYM_URL)

# get to login screen
join_btn = driver.find_element(By.CLASS_NAME, 'Home_heroButton__3eeI3')
join_btn.click()

# log in
email_box = driver.find_element(By.ID, 'email-input')
password_box = driver.find_element(By.ID, 'password-input')
submit_btn = driver.find_element(By.ID, 'submit-button')

email_box.send_keys(ACCOUNT_EMAIL)
password_box.send_keys(ACCOUNT_PASSWORD)
submit_btn.click()

# check if logged in
schedule_link = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'schedule-link')))
assert schedule_link is not None
print('Logged in successfully!')
driver.quit()