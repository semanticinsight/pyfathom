import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
from .Logger import Logger


def createSparkSession():

    _spark = SparkSession\
    .builder\
    .master("local")\
    .appName("Fathom.Configuration")\
    .getOrCreate()

    _logOverride = os.getenv("LOGGINGLEVELOVERRIDE") 

    if _logOverride:
        _spark.sparkContext.setLogLevel(_logOverride)

    def _createSparkSession():
      return _spark

    return _createSparkSession


def createLogger(printEnabled:bool=True):

    _spark = createSparkSession()()
    _logger = Logger(_spark, printEnabled)

    def _createLogger():
      return _logger
    
    return _createLogger


def createDbutils(environment:str, sparkSession:SparkSession):

    if (environment == "LOCALDEV"):

        dbutils = DBUtils(sparkSession)

    else:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]

    return dbutils


def getLogger(printEnabled:bool=True):
  return createLogger(printEnabled)()


def getSparkSession():
  return createSparkSession()()


def getDbutils(environment:str):
  
    if (environment == "LOCALDEV"):

        dbutils = DBUtils(getSparkSession())

    else:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]

    return dbutils