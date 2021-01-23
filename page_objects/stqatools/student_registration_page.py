from selenium.webdriver.common.by import By


class StudentRegistrationPage:
    st_name = (By.CSS_SELECTOR, "#studentname")
    father_name = (By.CSS_SELECTOR, "#fathername")
    post_addr = (By.ID, "paddress")
    personal_addr = (By.NAME, "personaladdress")
    sex = (By.CSS_SELECTOR, "input[value='male']")
    city = (By.NAME, "City")
    course = (By.NAME, "Course")
    district = (By.NAME, "District")
    state = (By.NAME, "State")
    pin_code = (By.ID, "pincode")
    email = (By.NAME, "emailid")
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def input_data(self):
        self.driver.find_element(*StudentRegistrationPage.st_name).send_keys("Mir")
        self.driver.find_element(*StudentRegistrationPage.father_name).send_keys("Richard")
        self.driver.find_element(*StudentRegistrationPage.post_addr).send_keys("12034 TX, Delhi")
        self.driver.find_element(*StudentRegistrationPage.personal_addr).send_keys("645 ACX, Mumbai")
        self.driver.find_element(*StudentRegistrationPage.sex).click()


