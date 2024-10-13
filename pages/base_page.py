import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

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

    def switch_to_new_window(self):
        self.wait.until(
            EC.new_window_is_opened,
            message="Error in switching to new window"
        )

        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)

    def switch_frames(self, *locator):
        frame1 = self.find_element(*locator)
        self.driver.switch_to.frame(frame1)

    def reset_frame(self):
        self.driver.switch_to.default_content()

    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()

    def presence_of_element_located(self, *locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Couldn't find the presence of element at '{locator}'")

    def get_attribute_value(self, *locator, attribute):
        actual_text = self.driver.find_element(*locator).get_attribute("value")
        return actual_text

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

    # def verify_by_webelement(self, element, expected_text):
    #     actual_text = element.text
    #     assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def select_dropdown_value(self, value, *locator):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_visible_text(value)

    def get_dropdown_value(self, value, *locator):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        selected_text = select.first_selected_option.text
        assert value == selected_text, f"Expected {value} but got {selected_text}"

    def checkbox_click(self, *locator):
        chkbox_element = self.driver.find_element(*locator)
        if chkbox_element.is_selected() != True:
            chkbox_element.click()


    def is_checkbox_selected(self, *locator):
        chkbox_element = self.driver.find_element(*locator)
        assert chkbox_element.is_selected() == True, f"Checkbox needs to selected!"

    def pagination(self, first_value, final_value, incremental, *locator):
        for i in range(first_value, final_value, incremental):
            self.click(*locator)
            time.sleep(2)







