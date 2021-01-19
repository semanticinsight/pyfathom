import os
import re
from .SparkContext import getSparkSession, getLogger, getDbutils


def _getEnv(variable:str): 

    var = os.getenv(variable)

    if var:
      return var

    else:
        msg = f"Environment variable '{variable}' not found"
        logger = getLogger()
        logger.logError(msg)

        raise Exception(msg)    


def getDbUtilsToken(): 

    return _getEnv("DBUTILSTOKEN")


def getOAuthRefreshUrl():

    return f"https://login.microsoftonline.com/{getAzureADId()}/oauth2/token"  


def getStorageAccount():

    return _getEnv("DATALAKESTORAGEACCOUNT")


def getEnvironment():

    return _getEnv("ENVIRONMENT")


def getAzureADId():

    return _getEnv("AZUREADID")


def getAutomationScope():

    return _getEnv("AUTOMATIONSCOPE")


def getDataLakeStorageType(): 

    return _getEnv("DATALAKESTORAGE") 


def getResourceGroup(): 

    return _getEnv("RESOURCEGROUP") 


def getSubscriptionId(): 

    return _getEnv("SUBSCRIPTIONID") 


def _getDbUtilsSecret(key:str): 

    dbutils = getDbutils(getEnvironment())

    secret = dbutils.secrets.get(
        scope = getAutomationScope(), 
        key = _getEnv(key))
        
    return secret


def getServicePrincipalId():

    return _getDbUtilsSecret("DATALAKESPNAPPID")


def getServiceObjectId():

    return _getDbUtilsSecret("DATALAKESPNOBJECTID")


def getServiceCredential():

    return _getDbUtilsSecret("DATALAKESPNCREDENTIAL")   


def getDatalakeConnectionString():

    return _getDbUtilsSecret("DATALAKECONNECTIONSTRING")  


def stripMargin(text):

    return re.sub('\n[ \t]*\|', '\n', text)


def help():

      return f"""
      <p>Configuration:</p>
      <table>
      <tr><th align='left'>Function          </th><th align='left'> Value               </td></tr>
      <tr><td>getEnvironment()               </td><td> {getEnvironment()}               </td></tr>
      <tr><td>getStorageAccount()            </td><td> {getStorageAccount()}            </td></tr>
      <tr><td>getDataLakeStorageType()       </td><td> {getDataLakeStorageType()}       </td></tr>
      <tr><td>getAutomationScope()           </td><td> {getAutomationScope()}           </td></tr>
      <tr><td>getResourceGroup()             </td><td> {getResourceGroup()}             </td></tr>
      <tr><td>getAzureADId()                 </td><td> {getAzureADId()}                 </td></tr>
      <tr><td>getSubscriptionId()            </td><td> {getSubscriptionId()}            </td></tr>
      <tr><td>getOAuthRefreshUrl()           </td><td> {getOAuthRefreshUrl()}           </td></tr>
      <tr><td>getServicePrincipalId()        </td><td> {getServicePrincipalId()}        </td></tr>
      <tr><td>getServiceObjectId()           </td><td> {getServiceObjectId()}           </td></tr>
      <tr><td>getServiceCredential()         </td><td> {getServiceCredential()}         </td></tr>
      <tr><td>getDatalakeConnectionString()  </td><td> {getDatalakeConnectionString()}  </td></tr>
      </table>
      """
