import pytest
from selenium import webdriver

URL = "https://stqatools.com/demo/index.php"
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser-name")
    global driver
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="../../drivers/geckodriver.exe")
    driver.maximize_window()
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.close()
