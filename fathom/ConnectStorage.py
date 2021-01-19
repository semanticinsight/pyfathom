from .Configuration import *
from .SparkContext import getSparkSession, getLogger

def ConnectStorage():

    _spark = getSparkSession()
    _logger = getLogger()

    _gen1 = "dfs.adls.oauth2"
    _gen2 = "fs.azure.account"

    _storageType = getDataLakeStorageType()

    if _storageType == "AzureDataLakeGen1":

      _spark.conf.set(f"{_gen1}.access.token.provider.type", "ClientCredential")
      _spark.conf.set(f"{_gen1}.client.id", getServicePrincipalId())
      _spark.conf.set(f"{_gen1}.credential", getServiceCredential())
      _spark.conf.set(f"{_gen1}.refresh.url", getOAuthRefreshUrl())    

    elif _storageType == "AzureDataLakeGen2":

      _spark.conf.set(f"{_gen2}.auth.type", "OAuth")
      _spark.conf.set(f"{_gen2}.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
      _spark.conf.set(f"{_gen2}.oauth2.client.id", getServicePrincipalId())
      _spark.conf.set(f"{_gen2}.oauth2.client.secret", getServiceCredential())
      _spark.conf.set(f"{_gen2}.oauth2.client.endpoint", getOAuthRefreshUrl())
    
    else:

        logError(f"Unknown storage type {_storageType} in enviornment variable DATALAKESTORAGE")
        raise Exception(f"Unknown storage type {_storageType} in enviornment variable DATALAKESTORAGE")   
    
    
    _logger.logInfo(stripMargin(f"""
      |Connected:
      |-----------------------------------------------
      | environment = {getEnvironment()}
      | storage account = {getStorageAccount()} 
    """))

