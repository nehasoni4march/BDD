from selenium.webdriver.common.by import By

from utils.BasePage import BasePage


class LoginPage(BasePage):
    TXT_USERNAME = (By.ID, "user-name")
    TXT_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    MSG_INVALIDCREDS = (By.ID, "//div[@class='error-message-container error']")

    def __init__(self, driver, job_id):
        super().__init__(driver, job_id)
        self.job_id = job_id

    def validateTitle(self):
        assert self.do_get_title() == "Swag Labs"

    def enter_login_credentials(self, user, pwd):
        self.do_sendkeys(self.TXT_USERNAME, user)
        self.do_sendkeys(self.TXT_PASSWORD, pwd)

    def enter_login(self):
        self.do_click(self.BTN_LOGIN, "LoginBtn")

    def validateInvalidCreds(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS, "Toast Item") == "Invalid credentials"

    def validateEmptyUsername(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS, "Toast Item") == "Username cannot be empty"

    def validateEmptyPassword(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS, "Toast Item") == "Password cannot be empty"
