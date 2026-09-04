from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpacSearchPage(BasePage):
    """Page Object representing the OPAC Catalog Search Interface."""

    # Locators (adjust DOM selectors according to your target UI)
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESULT_ITEMS = (By.CLASS_NAME, "book-item")
    NO_RESULTS_ALERT = (By.CSS_SELECTOR, ".alert-no-results")

    def __init__(self, driver):
        super().__init__(driver)

    def search_catalog(self, query: str):
        """Execute a catalog search using a title, author, or ISBN."""
        self.send_keys(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    def get_results_count(self) -> int:
        """Return the total number of search result items displayed."""
        results = self.driver.find_elements(*self.RESULT_ITEMS)
        return len(results)

    def is_no_results_message_visible(self) -> bool:
        """Check if the empty search result indicator is displayed."""
        return self.find(self.NO_RESULTS_ALERT).is_displayed()