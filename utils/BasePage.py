import time

from selenium.common import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from utils.constant import *
from utils.logger import *


class BasePage:

    def __init__(self, driver, job_id):
        self.job_id = job_id
        self.driver = driver

    def do_click(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        self.driver.find_element(*by_locator).click()
        logger(f"{element_name}  Clicked", LOGINFO, self.job_id)

    def do_sendkeys(self, by_locator, text_string):
        self.wait_until_element_visible(by_locator)
        self.driver.find_element(*by_locator).send_keys(text_string)
        logger(f"{text_string}  provided as input", LOGINFO, self.job_id)

    def do_clear(self, by_locator):
        self.wait_until_element_visible(by_locator)
        self.driver.find_element(*by_locator).clear()

    def do_select_by_text(self, by_locator, text):
        self.wait_until_element_visible(by_locator)
        select_obj = Select(self.driver.find_element(*by_locator))
        select_obj.select_by_visible_text(text)
        logger(f"{text}  Selected", LOGINFO, self.job_id)

    def do_select_by_index(self, by_locator, index):
        self.wait_until_element_visible(by_locator)
        select_obj = Select(self.driver.find_element(*by_locator))
        select_obj.select_by_index(index)
        logger(f"{index}  Item Selected", LOGINFO, self.job_id)

    def do_select_by_value(self, by_locator, value):
        self.wait_until_element_visible(by_locator)
        select_obj = Select(self.driver.find_element(*by_locator))
        select_obj.select_by_value(value)
        logger(f"{value}  Selected", LOGINFO, self.job_id)

    def do_get_title(self):
        title = str(self.driver.title).strip()
        logger(f"Title is : {title}", LOGINFO, self.job_id)
        return title

    def do_submit(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        self.driver.find_element(*by_locator).submit()
        logger(f"{element_name}  Submitted", LOGINFO, self.job_id)

    def find_element(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        element = self.driver.find_element(*by_locator)
        return element

    def find_elements(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        elements = self.driver.find_elements(*by_locator)
        return elements

    """ Wait Methods"""

    def generic_wait(self):
        self.driver.implicitly_wait(GENERIC_WAIT)

    def force_wait_with_generic_time(self):
        time.sleep(GENERIC_WAIT)

    def force_wait(self, wait_time):
        time.sleep(wait_time)

    def fluent_wait(self):
        return WebDriverWait(self.driver, GENERIC_WAIT, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 StaleElementReferenceException])

    def wait_until_element_presence(self, by_locator):
        self.fluent_wait().until(EC.presence_of_element_located(by_locator))

    def wait_until_element_visible(self, by_locator):
        self.fluent_wait().until(EC.visibility_of_element_located(by_locator))

    def wait_until_element_clickable(self, by_locator):
        self.fluent_wait().until(EC.element_to_be_clickable(by_locator))

    def wait_until_iframe_available_switch(self, by_locator):
        self.fluent_wait().until(frame_to_be_available_and_switch_to_it(by_locator))

    def open_application(self, url, application_name=""):
        self.driver.get(url)
        self.generic_wait()
        logger(f"{application_name} opened", LOGINFO, self.job_id)

    def is_element_visible(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        is_element_displayed = self.driver.find_element(*by_locator).is_displayed()
        logger(f"{element_name} is displayed: {is_element_displayed}", LOGINFO, self.job_id)
        return is_element_displayed

    def is_element_selected(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        is_element_selected = self.driver.find_element(*by_locator).is_selected()
        logger(f"{element_name} is selected: {is_element_selected}", LOGINFO, self.job_id)
        return is_element_selected

    def is_element_enabled(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        is_element_enable = self.driver.find_element(*by_locator).is_enabled()
        logger(f"{element_name} is enabled: {is_element_enable}", LOGINFO, self.job_id)
        return is_element_enable

    def get_element_text(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        get_text = self.driver.find_element(*by_locator).text
        logger(f"Text Fetched:{get_text}", LOGINFO, self.job_id)
        return get_text

    def get_element_property(self, by_locator, property_type, element_name=""):
        self.wait_until_element_visible(by_locator)
        get_property_info = self.driver.find_element(*by_locator).get_property(property_type)
        logger(f"From {element_name} got property of : {get_property_info}", LOGINFO, self.job_id)
        return get_property_info

    def get_element_attribute(self, by_locator, property_type, element_name=""):
        self.wait_until_element_visible(by_locator)
        attribute_info = self.driver.find_element(*by_locator).get_attribute(property_type)
        logger(f"From {element_name} got attribute of : {attribute_info}", LOGINFO, self.job_id)
        return attribute_info

    def take_page_screenshot(self, filename):
        screenshot_name = filename + "png"
        screenshot_folder = os.getcwd() + os.sep + "reports" + os.sep + self.job_id + os.sep + "screenshots"
        if not os.path.isdir(screenshot_folder):
            os.makedirs(screenshot_folder)
        screenshot_file = screenshot_folder + os.sep + screenshot_name
        self.driver.save_screenshot(screenshot_file)

    def take_element_screenshot(self, by_locator, filename):
        screenshot_file = os.getcwd() + os.sep + "logs" + os.sep + self.job_id + os.sep + filename + ".png"
        self.driver.find_element(*by_locator).screenshot(screenshot_file)

    def get_element_size(self, by_locator, element_name=""):
        self.wait_until_element_visible(by_locator)
        size = self.driver.find_element(*by_locator).size()
        logger(f"From {element_name} size is : {size}", LOGINFO, self.job_id)
        return size

    def switch_to_iframe(self, by_locator, frame_name):
        self.wait_until_iframe_available_switch(by_locator)
        logger(f"Switch to iframe: {frame_name}", LOGINFO, self.job_id)

    def switch_to_child_window(self, window_name):
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for w in all_windows:
            if w != current_window:
                self.driver.switch_to_window(w)
                logger(f"Switch to window : {window_name} ", LOGINFO, self.job_id)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        logger(f"Switch to default content", LOGINFO, self.job_id)

    def validate_list_data(self, actual_data_list, expected_data_list):
        status = True
        for data in actual_data_list:
            if data not in expected_data_list:
                logger(f"{data} not in {expected_data_list}", LOGINFO, self.job_id)
                status = False
        return status

    def validate_dict_data(self, actual_data, expected_data):
        status = True
        if actual_data != expected_data:
            logger("Expected data is not matched with actual data", LOGINFO, self.job_id)
            status = False
            return status
        logger("Validated WAC details with ILO details successfully data is matched ", LOGINFO, self.job_id)
        return status

    def get_list_of_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)
