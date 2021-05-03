import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
