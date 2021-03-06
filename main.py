from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from os import mkdir, rmdir


class GoogleKeywordScreenshooter:
    def __init__(self, keyword, screenshots_dir):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        self.keyword = keyword
        try:
            mkdir(f"screenshots/search/{self.keyword}")
        except Exception:
            rmdir(f"screenshots/search/{self.keyword}")
            mkdir(f"screenshots/search/{self.keyword}")
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            #question_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cUnQKe")))
            question_box = self.browser.find_element_by_class_name("cUnQKe")
            self.browser.execute_script(
                """
                const questionBox = arguments[0];
                questionBox.parentElement.removeChild(questionBox);
                """, question_box)
        except Exception:
            pass
        search_results = self.browser.find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
            if search_result.get_attribute("class") == "g":
                search_result.screenshot(
                    f"{self.screenshots_dir}/search/{self.keyword}/{self.keyword}x{index}.png")

    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()
