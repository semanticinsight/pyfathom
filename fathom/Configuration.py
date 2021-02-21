import os
from .SparkContext import get_spark_session, get_logger, get_dbutils


def _get_env(variable:str): 

    var = os.getenv(variable)

    if var:
      return var

    else:
        msg = f"Environment variable '{variable}' not found"
        logger = get_logger()
        logger.log_error(msg)

        raise Exception(msg)    


def get_oauth_refresh_url():

    return f"https://login.microsoftonline.com/{get_azure_ad_id()}/oauth2/token"  


def get_storage_account():

    return _get_env("STORAGEACCOUNT")


def get_environment():

    return _get_env("ENVIRONMENT")


def get_azure_ad_id():

    return _get_env("AZUREADID")


def get_automation_scope():

    return _get_env("AUTOMATIONSCOPE")


def get_dataLake_storage_type(): 

    return _get_env("STORAGE") 


def get_resource_group(): 

    return _get_env("RESOURCEGROUP") 


def get_subscription_id(): 

    return _get_env("SUBSCRIPTIONID") 


def _get_dbutils_secret(key:str): 

    dbutils = get_dbutils(get_environment())

    secret = dbutils.secrets.get(
        scope = get_automation_scope(), 
        key = _get_env(key))
        
    return secret


def get_service_principal_id():

    return _get_dbutils_secret("DATAPLATFORMAPPID")


def get_service_credential():

    return _get_dbutils_secret("DATAPLATFORMSECRET")   




def help(as_html=False):
    
    if as_html:
      return f"""
      <p>Configuration:</p>
      <table>
      <tr><th align='left'>Function          </th><th align='left'> Value               </td></tr>
      <tr><td>get_environment()              </td><td> {get_environment()}              </td></tr>
      <tr><td>get_storage_account()          </td><td> {get_storage_account()}          </td></tr>
      <tr><td>get_dataLake_storage_type()    </td><td> {get_dataLake_storage_type()}       </td></tr>
      <tr><td>get_automation_scope()         </td><td> {get_automation_scope()}           </td></tr>
      <tr><td>get_resource_group()           </td><td> {get_resource_group()}             </td></tr>
      <tr><td>get_azure_ad_id()              </td><td> {get_azure_ad_id()}              </td></tr>
      <tr><td>get_subscription_id()          </td><td> {get_subscription_id()}            </td></tr>
      <tr><td>get_oauth_refresh_url()        </td><td> {get_oauth_refresh_url()}        </td></tr>
      <tr><td>get_service_principal_id()     </td><td> {get_service_principal_id()}        </td></tr>
      <tr><td>get_service_credential()       </td><td> {get_service_credential()}         </td></tr>
      </table>
      """
    else:
        print(f"""
Configuration:
--------------------------------------------------------
get_environment()           : {get_environment()} 
get_storage_account()       : {get_storage_account()}        
get_dataLake_storage_type() : {get_dataLake_storage_type()}     
get_automation_scope()      : {get_automation_scope()}        
get_resource_group()        : {get_resource_group()}          
get_azure_ad_id()           : {get_azure_ad_id()}            
get_subscription_id()       : {get_subscription_id()}          
get_oauth_refresh_url()     : {get_oauth_refresh_url()}      
get_service_principal_id()  : {get_service_principal_id()}       
get_service_credential()    : [REDACTED]  
        """)
