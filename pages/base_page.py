from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class containing core web interactions for all Page Objects."""
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def find(self, locator: tuple):
        """Wait for an element to be present in the DOM and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: tuple, text: str):
        """Wait for an input field to be visible, clear it, and type text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Fetch text content from a visible element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text