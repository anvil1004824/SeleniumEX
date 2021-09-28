from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os import mkdir, rmdir


class ResponsiveTester:
    def __init__(self, urls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        self.browser.get(url)
        url = url.replace("https://", "").replace(".", "-")
        try:
            mkdir(f"screenshots/responsive/{url}")
        except Exception:
            rmdir(f"screenshots/responsive/{url}")
            mkdir(f"screenshots/responsive/{url}")

        BROWSER_HEIGHT = self.browser.execute_script(
            "return window.innerHeight")

        for size in self.sizes:
            self.browser.set_window_size(
                size, self.browser.get_window_size()["height"])
            self.browser.execute_script("window.scrollTo(0, 0)")
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            total_sections = ceil(scroll_size/BROWSER_HEIGHT)
            for section in range(total_sections):
                self.browser.execute_script(
                    f"window.scrollTo(0, {(section)*BROWSER_HEIGHT})")
                time.sleep(0.5)
                self.browser.save_screenshot(
                    f"screenshots/responsive/{url}/{size}x{section}.png")

    def start(self):
        for url in self.urls:
            self.screenshot(url)
        self.browser.quit()


tester = ResponsiveTester(["https://nomadcoders.co", "https://google.com"])
tester.start()
