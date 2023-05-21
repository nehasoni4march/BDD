from selenium.webdriver.common.by import By

from utils.BasePage import BasePage


class DashboardPage(BasePage):
    TXT_DASHBOARD = (By.XPATH, "//span[contains(text(),'Products')]")

    def __init__(self, driver, job_id):
        super().__init__(driver, job_id)
        self.job_id = job_id

    def validate_home_page(self):
        # self.is_element_visible(self.TXT_DASHBOARD, "Header")
        assert self.get_element_text(self.TXT_DASHBOARD, "Header").lower() == "products"
