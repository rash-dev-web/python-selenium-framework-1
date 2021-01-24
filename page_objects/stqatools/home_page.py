from selenium.webdriver.common.by import By

from page_objects.stqatools.web_table_page import WebTable


class HomePage:
    web_table = (By.LINK_TEXT, "WebTable")

    def __init__(self, driver):
        self.driver = driver

    def click_web_table(self):
        self.driver.find_element(*HomePage.web_table).click()
        return WebTable(self.driver)

