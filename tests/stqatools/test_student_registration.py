import pytest

from page_objects.stqatools.student_registration_page import StudentRegistrationPage


class TestStudentRegistration:
    @pytest.mark.usefixtures("setup")
    def test_submit_form(self):
        st_registration_page = StudentRegistrationPage(self.driver)
        email_text = st_registration_page.input_data()
        assert email_text == ""




