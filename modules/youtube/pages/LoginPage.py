from selenium.webdriver.common.by import By

from utils.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBTN = (By.ID, "login-button")

    def __init__(self, driver, job_id):
        self.job_id = job_id
        super().__init__(driver, job_id)

    def validate_portal_title(self):
        actualTitle = self.do_get_title()
        assert actualTitle == "YouTube"
