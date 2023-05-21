import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.youtube.configuration.variables import *
from modules.youtube.pages.LoginPage import LoginPage
from utils.constant import *


@when(u'I launch the browser')
def step_impl(context):
    if BROWSER == "chrome":
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        context.driver = webdriver.Chrome(executable_path=CHROMEDRIVE, chrome_options=options)
    else:
        print("Browser Not Supported !")


@then(u'I open the portal')
def step_impl(context):
    context.driver.get(URL)
    context.LoginPage = LoginPage(context.driver, context.job_id)


@then(u'I validated the portal opened')
def step_impl(context):
    context.LoginPage.validate_portal_title()

