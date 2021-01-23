from selenium.webdriver.support.select import Select
import pytest

from page_objects.stqatools.student_registration_page import StudentRegistrationPage


class TestStudentRegistration:
    @pytest.mark.usefixtures("setup")
    def test_submit_form(self):
        st_registration_page = StudentRegistrationPage(self.driver)
        st_registration_page.input_data()

        select_city = Select(self.driver.find_element_by_name("City"))
        select_city.select_by_visible_text("MUMBAI")
        select_course = Select(self.driver.find_element_by_name("Course"))
        select_course.select_by_visible_text("MBA")
        select_district = Select(self.driver.find_element_by_name("District"))
        select_district.select_by_index(3)
        select_state = Select(self.driver.find_element_by_name("State"))
        select_state.select_by_value("Goa")
        self.driver.find_element_by_id("pincode").send_keys("357932")
        self.driver.find_element_by_name("emailid").send_keys("abc@email.com")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        assert self.driver.find_element_by_name("emailid").text == ""




