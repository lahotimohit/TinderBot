from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://tinder.com/"
EMAIL = "engtesting23@gmail.com"
PASSWORD = "**********"

driver.get(url=URL)
driver.maximize_window()
base_window = driver.window_handles[0]

time.sleep(3)

Log_In = driver.find_element(By.LINK_TEXT, "Log in")
Log_In.click()

time.sleep(3)

facebook_login = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_login.click()

time.sleep(6)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)

email_add = driver.find_element(By.ID, "email")
email_add.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)

submit_btn = driver.find_element(By.NAME, "login")
submit_btn.click()

driver.switch_to.window(base_window)
time.sleep(5)

# Allows Location
location = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()

time.sleep(3)

notifications = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
notifications.click()

time.sleep(3)

cookies = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

time.sleep(3)

for n in range(40):
    time.sleep(1)
    try:
        print("Like button display")
        like_btn = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
        like_btn.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
          
input(Keys.ENTER)
driver.quit()
