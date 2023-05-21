import os
import traceback
from datetime import datetime

LOGINFO = 1
LOGERROR = 2
LOGDEBUG = 3

logDict = {
    LOGINFO: "INFO",
    LOGERROR: "ERROR",
    LOGDEBUG: "DEBUG"

}


def logger(logString, LOGLEVEL, job_id, print_log=True):
    try:
        debuglogFile = os.getcwd() + os.sep + "logs" + os.sep + job_id + os.sep + job_id + ".log"
        if not os.path.isdir(os.path.dirname(debuglogFile)):
            os.makedirs(os.path.dirname(debuglogFile))

        if not os.path.isfile(debuglogFile):
            f = open(debuglogFile, "w")
            f.close()

        if print_log:
            print(logString)
        TS = str(datetime.now())
        custom_logstring = f"{TS} - {logDict[LOGLEVEL]} - {logString}"
        f = open(debuglogFile, "a")
        f.write(custom_logstring + "\n")
        f.close()
    except:
        pass


def catch_detailed_exception(job_Id):
    '''
    This method is used to traceback the failed reason with all neccessary details.
    :param job_Id:
    :return:
    '''
    try:
        logger("Inside catch_detailed_exception", LOGERROR, job_Id)
        logger(traceback.format_exc(), LOGERROR, job_Id)
    except:
        pass
