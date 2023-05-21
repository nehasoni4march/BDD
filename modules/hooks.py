from utils.constant import *
from utils.logger import *
import allure
from allure_commons.types import AttachmentType
from utils.utils import Utils


def before_all(context):
    context.job_id = context.config.userdata['job_id']
    context.modulename = context.config.userdata['module']

    context.utils = Utils(context.job_id)
    logger(f" Behave Env JobId:{context.job_id} || module:{context.modulename} ", LOGINFO, context.job_id)


def before_feature(context, feature):
    logger(f" [FEATURE]:{feature.name} ".center(80, "*"), LOGINFO, context.job_id)


def before_scenario(context, scenario):
    logger(f"\n[SCENARIO]:{scenario.name}", LOGINFO, context.job_id)


def before_step(context, step):
    pass


""" After Logic"""


def after_all(context):
    context.utils.copy_allure_serve_batchfile()
    pass


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    STATUS = str(scenario.status).replace("Status.", "").strip().upper()

    """Attaching the screensot to the allure report"""
    if STATUS.__eq__("FAILED"):
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        logger(f"STATUS:FAILED\n", LOGINFO, context.job_id)
    else:
        logger(f"STATUS:PASSED\n", LOGERROR, context.job_id)

    """Attaching the execution log the allure report"""
    debuglogFile = "logs" + os.sep + context.job_id + os.sep + context.job_id + ".log"  # execution log file path
    with open(debuglogFile) as f:
        data = f.read()
    allure.attach(str(data), name="Console Logs", attachment_type=AttachmentType.TEXT)

    """ Close the driver after each sceanrio"""
    context.driver.close()


def after_step(context, step):
    STATUS = str(step.status).replace("Status.", "").strip().upper()
    logger(f"[STEP]:{step.name} - {STATUS}", LOGINFO, context.job_id)
