from pyspark.sql import SparkSession
import os
import re

class Logger:

    def __init__(self, spark:SparkSession, printEnabled:bool=True):

        self.logLevelOverride = os.getenv("LOGGINGLEVELOVERRIDE")
        self._log4jLogger = spark._jvm.org.apache.log4j
        self._logger = self._log4jLogger.LogManager.getRootLogger()

        self.printEnabled = printEnabled      
        
        if self.logLevelOverride:
            self.printEnabled = True

    def log_info(self, message:str):

        if (self.printEnabled):
            print(self._strip_margin(message))

        self._logger.info(message)      

    def log_error(self, message:str):

        if (self.printEnabled):
            print(self._strip_margin(message))

        self._logger.error(message)


    def _strip_margin(self, text):

        return re.sub('\n[ \t]*\|', '\n', text)