from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class SwitchToPage:

    def __init__(self, driver):
        self.driver = driver

    # java script elements
    js_basic_alert = (By.CSS_SELECTOR, "#jbalert")
    js_confirm_alert = (By.CSS_SELECTOR, "#jcalert")
    js_prompt_alert = (By.CSS_SELECTOR, "#jpalert")

    # bootstrap alert
    bs_basic_alert = (By.ID, "btnAlert")
    bs_confirm_alert = (By.ID, "btnConfirm")
    bs_prompt_alert = (By.ID, "btnPrompt")

    def click_basic_alert(self):
        self.driver.find_element(*SwitchToPage.js_basic_alert).click()
        js_alert = self.driver.switch_to.alert
        alert_text = js_alert.text
        js_alert.accept()
        return alert_text

