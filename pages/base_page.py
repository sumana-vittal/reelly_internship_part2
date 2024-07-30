from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        ).click()

    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()

    def presence_of_element_located(self, *locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Couldn't find the presence of element at '{locator}'")

    def verify_attribute_value(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).get_attribute("value")
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_url(self, expected_url_text):
        self.wait.until(EC.url_contains(expected_url_text),
                        message = f"Expected text '{expected_url_text}' not part of url!")




