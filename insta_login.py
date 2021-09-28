import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def insta_login(browser):
    INSTAGRAM_ID = input("Enter Your INSTAGRAM ID : ")
    INSTAGRAM_PASSWORD = input("Enter Your INSTAGRAM password : ")

    browser.get("https://www.instagram.com/accounts/login/")

    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ")))

    insta_id = browser.find_element_by_name("username")
    insta_password = browser.find_element_by_name("password")

    insta_id.send_keys(INSTAGRAM_ID)
    insta_password.send_keys(INSTAGRAM_PASSWORD)

    insta_password.send_keys(Keys.ENTER)

    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "qNELH")))
