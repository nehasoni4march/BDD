import os
import shutil

from utils.constant import *
from utils.logger import *


class Utils:

    def __init__(self, job_id):
        self.job_id = job_id

    def execute_by_feature_file_param(self, module_name, feature_files):
        """
        Return feature execution params.
        :param module_name:
        :param feature_files: For multiple feature files, separtae them using comma (,) Eg: youtube.feature,dashboard.feature
        :return:
        """
        self.feature_exec_param = []
        self.feature_files_list = []
        featurefile_loc = f".\\modules\\{module_name}\\features\\"
        if str(feature_files).__contains__(","):
            self.feature_files_list = str(feature_files).split(",")
            for feature in self.feature_files_list:
                self.feature_exec_param.append(f"{featurefile_loc}{feature}")

            print("self.feature_exec_param:", self.feature_exec_param)
            self.feature_exec_param = " ".join(self.feature_exec_param)
        else:
            self.feature_exec_param = (f"{featurefile_loc}{feature_files}")
        return self.feature_exec_param

    def copy_files(self, source, destination):
        """
        This method can be used to copy the whole file from source to the destination.
        :param source:
        :param destination:
        :return:
        """
        try:
            if not os.path.exists(destination):
                os.makedirs(destination)
                logger("Creating folder as it doesn't exist previously", LOGINFO, self.job_id)
            shutil.copy(source, destination)
            logger("Copying file:{0} ==>{1}".format(source, destination), LOGINFO, self.job_id, print_log=False)
            return True
        except:
            catch_detailed_exception(self.job_id)
            return False

    def copy_directories(self, source, destination):
        """
        This method can be used to copy the whole directory from source to the destination.
        :param source:
        :param destination:
        """
        try:
            self.copytree(source, destination, symlinks=False, ignore=None)
            logger("Copying Dir:{0} ==>> {1}".format(source, destination), LOGDEBUG,
                   self.job_id, print_log=False)
            return True
        except:
            catch_detailed_exception(self.job_id)
            return False

    def copytree(self, source, destination, symlinks=False, ignore=None):
        """
        This helper method is used to copy the files/directory
        :param source:
        :param destination:
        """
        if not os.path.exists(destination):
            os.makedirs(destination)
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                self.copytree(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)

    def copy_allure_serve_batchfile(self):
        """
        Method to transfer the AllureServe.bat file from resources directory to the report for user ease
        to see the allure report
        :return:
        """

        result_path = "reports" + os.sep + self.job_id
        self.copy_files(ALLURE_REPORT_BATCHFILE, result_path)
