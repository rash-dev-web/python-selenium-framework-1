from selenium.webdriver.common.by import By

from page_objects.stqatools.switch_to_page import SwitchToPage
from page_objects.stqatools.web_table_page import WebTable
import time


class HomePage:
    web_table = (By.LINK_TEXT, "WebTable")
    switch_to = (By.XPATH, "//a[contains(text(),'Switch To')]")
    alert = (By.CSS_SELECTOR, "a[href='Alerts.php']")

    def __init__(self, driver):
        self.driver = driver

    def click_web_table(self):
        self.driver.find_element(*HomePage.web_table).click()
        return WebTable(self.driver)

    def click_switch_to(self):
        switch_to_ele = self.driver.find_element(*HomePage.switch_to)
        switch_to_ele.click()
        # print("switch to clicked...")

    def click_alert(self):
        self.click_switch_to()
        time.sleep(5)
        self.driver.find_element(*HomePage.alert).click()
        return SwitchToPage(self.driver)



