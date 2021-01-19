from pyspark.sql import SparkSession
import os

class Logger:

    def __init__(self, spark:SparkSession, printEnabled:bool=True):

        self.logLevelOverride = os.getenv("LOGGINGLEVELOVERRIDE")
        self._log4jLogger = spark._jvm.org.apache.log4j
        self._logger = self._log4jLogger.LogManager.getRootLogger()

        self.printEnabled = printEnabled      
        
        if self.logLevelOverride:
            self.printEnabled = True

    def logInfo(self, message:str):

        if (self.printEnabled):
            print(message)

        self._logger.info(message)      

    def logError(self, message:str):

        if (self.printEnabled):
            print(message)

        self._logger.error(message)