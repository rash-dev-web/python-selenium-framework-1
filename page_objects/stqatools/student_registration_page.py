from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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
        select_city = Select(self.driver.find_element(*StudentRegistrationPage.city))
        select_city.select_by_visible_text("MUMBAI")
        select_course = Select(self.driver.find_element(*StudentRegistrationPage.course))
        select_course.select_by_visible_text("MBA")
        select_district = Select(self.driver.find_element(*StudentRegistrationPage.district))
        select_district.select_by_index(3)
        select_state = Select(self.driver.find_element(*StudentRegistrationPage.state))
        select_state.select_by_value("Goa")

        self.driver.find_element(*StudentRegistrationPage.pin_code).send_keys("357932")
        self.driver.find_element(*StudentRegistrationPage.email).send_keys("abc@email.com")
        self.driver.find_element(*StudentRegistrationPage.submit_button).click()
        return self.driver.find_element(*StudentRegistrationPage.email).text



