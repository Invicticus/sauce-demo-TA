import pytest
import selenium.webdriver


# Initialize the WebDriver
@pytest.fixture
def driver():
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()
