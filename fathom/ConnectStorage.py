from .Configuration import *
from .SparkContext import get_spark_session, get_logger

def connect_storage():

    _spark = get_spark_session()
    _logger = get_logger()

    _gen1 = "dfs.adls.oauth2"
    _gen2 = "fs.azure.account"

    _storageType = get_dataLake_storage_type()

    if _storageType == "AzureDataLakeGen1":

      _spark.conf.set(f"{_gen1}.access.token.provider.type", "ClientCredential")
      _spark.conf.set(f"{_gen1}.client.id", get_service_principal_id())
      _spark.conf.set(f"{_gen1}.credential", get_service_credential())
      _spark.conf.set(f"{_gen1}.refresh.url", get_oauth_refresh_url())    

    elif _storageType == "AzureDataLakeGen2":

      _spark.conf.set(f"{_gen2}.auth.type", "OAuth")
      _spark.conf.set(f"{_gen2}.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
      _spark.conf.set(f"{_gen2}.oauth2.client.id", get_service_principal_id())
      _spark.conf.set(f"{_gen2}.oauth2.client.secret", get_service_credential())
      _spark.conf.set(f"{_gen2}.oauth2.client.endpoint", get_oauth_refresh_url())
    
    else:

        logError(f"Unknown storage type {_storageType} in enviornment variable DATALAKESTORAGE")
        raise Exception(f"Unknown storage type {_storageType} in enviornment variable DATALAKESTORAGE")   
    

    _logger.log_info(f"""
      |Connected:
      |-----------------------------------------------
      | environment = {get_environment()}
      | storage account = {get_storage_account()} 
    """)

