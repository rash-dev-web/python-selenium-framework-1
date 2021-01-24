import pytest
from selenium.webdriver import ActionChains

from page_objects.stqatools.home_page import HomePage
import time


class TestAlert:
    @pytest.mark.usefixtures("setup")
    def test_js_basic_alert(self):
        home_page = HomePage(self.driver)
        home_page.click_switch_to()
        alert_page = home_page.click_alert()
        time.sleep(3)
        alert_text = alert_page.click_basic_alert()
        time.sleep(3)
        assert alert_text == "This is Simple Javascript Alert"

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://stqatools.com/demo/index.php")
# time.sleep(3)
# switch_to_ele = driver.find_element_by_xpath("//a[contains(text(),'Switch To')]")
# # switch_to_ele = driver.find_element_by_css_selector(".nav-item.dropdown.show")
# switch_to_ele.click()
# # driver.execute_script("arguments[0].click()", switch_to_ele)
# # action = ActionChains(driver)
# # action.move_to_element(switch_to_ele).click()
# driver.find_element_by_link_text("Alert").click()
# time.sleep(3)
# driver.close()
