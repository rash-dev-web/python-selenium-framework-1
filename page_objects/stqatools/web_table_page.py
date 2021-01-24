from selenium.webdriver.common.by import By


class WebTable:
    def __init__(self, driver):
        self.driver = driver

    search_name = (By.CSS_SELECTOR, "#system-search")
    f_name = (By.XPATH, "//table//tr[@id='d1']/td[2]")
    l_name = (By.XPATH, "//table//tr[@id='d1']/td[3]")
    email = (By.XPATH, "//table//tr[@id='d1']/td[4]")

    def enter_name_search_box(self, search_name):
        self.driver.find_element(*WebTable.search_name).send_keys(search_name)

    def verify_user(self):
        user_data = [self.driver.find_element(*WebTable.f_name).text,
                     self.driver.find_element(*WebTable.l_name).text,
                     self.driver.find_element(*WebTable.email).text
                     ]
        return user_data



