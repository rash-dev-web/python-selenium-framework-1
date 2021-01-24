from page_objects.stqatools.home_page import HomePage

import pytest
import time


class TestWebTable:

    @pytest.mark.usefixtures("setup")
    def test_search_web_table(self):
        home_page = HomePage(self.driver)
        web_table = home_page.click_web_table()
        web_table.enter_name_search_box("Sameer")
        return web_table

    @pytest.mark.usefixtures("setup")
    def test_verify_user(self):
        web_table = self.test_search_web_table()
        user_list = web_table.verify_user()
        assert ["Sameer", "Patil", "s@gmail.com"] == user_list


