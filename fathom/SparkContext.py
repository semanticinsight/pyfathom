import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
from .Logger import Logger


def create_spark_session():

    _spark = SparkSession\
    .builder\
    .master("local")\
    .appName("fathom.Configuration")\
    .getOrCreate()

    _logOverride = os.getenv("LOGGINGLEVELOVERRIDE") 

    if _logOverride:
        _spark.sparkContext.setLogLevel(_logOverride)

    def _create_spark_session():
      return _spark

    return _create_spark_session


def create_logger(printEnabled:bool=True):

    _spark = create_spark_session()()
    _logger = Logger(_spark, printEnabled)

    def _create_logger():
      return _logger
    
    return _create_logger


def create_dbutils(environment:str):

    if (environment == "LOCALDEV"):

        # unfortunately the remote local runtime works differently using DBUtils than it does cluster side
        # so we have to detect the environment when running on db-connect locally to set the token and
        # dbutils accordingly - this handles local remote and cluster side execution.
        _dbutils = DBUtils(get_spark_session())
        _dbutils.secrets.setToken(os.getenv("DBUTILSTOKEN"))

    else:
        import IPython
        _dbutils = IPython.get_ipython().user_ns["dbutils"]

    def _create_dbutils():
        return _dbutils
        
    return _create_dbutils


def get_logger(printEnabled:bool=True):
  return create_logger(printEnabled)()


def get_spark_session():
  return create_spark_session()()


def get_dbutils(environment:str):
  
    return create_dbutils(environment)()