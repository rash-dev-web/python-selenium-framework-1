import pytest
from selenium import webdriver

URL = "https://stqatools.com/demo/index.php"


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.close()
