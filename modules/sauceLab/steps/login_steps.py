import time
from behave import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.sauceLab.configuration.variables import URL
from modules.sauceLab.pages.DashboardPage import DashboardPage
from modules.sauceLab.pages.LoginPage import LoginPage

from utils.constant import *
from utils.logger import *


@given(u'I Launch the browser')
def launch_browser(context):
    try:
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if BROWSER == 'chrome':
            context.driver = webdriver.Chrome(executable_path=CHROMEDRIVE, chrome_options=options)
        else:
            raise ValueError('Browser is not supported')
    except:
        catch_detailed_exception(context.job_id)
        assert False, "Failed! Unable to launch the browser"


@when(u'I Open the saucedemo website')
def open_login_page(context):
    try:
        context.driver.get(URL)
        context.loginPage = LoginPage(context.driver, context.job_id)
        context.dashboardpage = DashboardPage(context.driver, context.job_id)
    except:
        assert False, "Failed! Unable to open the portal. Check the network connectivity"


@then(u'The login portal has been opened')
def validate_login_page(context):
    try:
        context.loginPage.validateTitle()
    except:
        assert False, "Test is failed in validate login page title"


@given(u'I provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:
        context.loginPage.enter_login_credentials(user, pwd)
    except:
        assert False, "Test is failed in enter login credentials"


@when(u'I click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        assert False, "Test is failed in enter login"


@then(u'Validate login is successful')
def validate_dashboard_page(context):
    try:
        context.dashboardpage.validate_home_page()
        time.sleep(3)
    except:
        assert False, "Test is failed in validating dashboard"


@then(u'Close the browser')
def step_impl(context):
    try:
        context.driver.close()
    except:
        pass
