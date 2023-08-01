from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, *args):
        return self.driver.find_element(*args)

    def find_all(self, *args):
        return self.driver.find_elements(*args)
