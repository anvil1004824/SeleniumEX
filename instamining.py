import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from insta_login import insta_login

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def wait_for(locator):
    return WebDriverWait(browser, 10).until(EC.presence_of_element_located((locator)))


# insta_login(browser)

main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

header = wait_for((By.TAG_NAME, "header"))

post_count = wait_for((By.CLASS_NAME, "g47SY"))
if post_count:
    post_count = int(post_count.text.replace(",", ""))
    print(post_count)
