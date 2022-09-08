import pytest
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestYahoo:
    wait = None

    '''
    This fixture can be consumed by any test
    First the code before the yield executes
    Then you yield the driver, which can be used by consuming tests
    after the test completes, everything under the yield will execute
    '''
    @pytest.fixture
    def driver(self):
        path = r"C:\WebDrivers\chromedriver.exe"
        self.driver = wd.Chrome(executable_path=path)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield self.driver
        self.driver.quit()

    def test_yahoo_title(self, driver):
        driver.get('http://www.yahoo.com')
        assert 'Yahoo' in driver.title

    def test_yahoo_url(self, driver):
        driver.get('http://www.yahoo.com')
        assert 'https://www.yahoo.com' in driver.current_url

    def test_yahoo_search(self, driver):
        driver.get('http://www.yahoo.com')
        driver.find_element(By.ID, "ybar-sbq").send_keys("Eliza Fletcher" + Keys.ENTER)
        self.wait.until(EC.presence_of_element_located((By.ID, "results")))
        element = driver.find_element(By.ID, "results")
        assert "Top Stories" in element.text
