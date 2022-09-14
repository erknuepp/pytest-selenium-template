import pytest
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
import page

class TestYahoo:
    wait = None

    '''
    This fixture can be consumed by any test
    First the code before the yield executes
    Then you yield the driver, which can be used by consuming tests
    after the test completes, everything under the yield will execute
    '''
    @pytest.fixture
    def yahoo_driver(self):
        path = r"C:\WebDrivers\chromedriver.exe"
        s = Service(path)
        self.driver = wd.Chrome(service=s)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://www.yahoo.com')
        yield self.driver
        self.driver.quit()

    @pytest.fixture
    def python_driver(self):
        path = r"C:\WebDrivers\chromedriver.exe"
        s = Service(path)
        self.driver = wd.Chrome(service=s)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://www.python.org')
        yield self.driver
        self.driver.quit()

    def test_yahoo_title(self, yahoo_driver):
        assert 'Yahoo' in yahoo_driver.title

    def test_yahoo_url(self, yahoo_driver):
        assert 'https://www.yahoo.com' in yahoo_driver.current_url

    def test_yahoo_search(self, yahoo_driver):
        yahoo_driver.find_element(By.ID, "ybar-sbq").send_keys("Eliza Fletcher" + Keys.ENTER)
        self.wait.until(ec.presence_of_element_located((By.ID, "results")))
        element = yahoo_driver.find_element(By.ID, "results")
        assert "Top Stories" in element.text

    def test_python(self, python_driver):
        main_page = page.MainPage(python_driver)
        assert main_page.is_title_matches() is True
