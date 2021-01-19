
import fathom.Configuration as config
import os

def test_test():

    assert 1 == 1

def test_getEnv(): 

    variable = "FATHOM_CONFIG_TEST"
    expected = "1"
    os.environ[variable] = expected

    result = config._getEnv(variable)
    
    del os.environ[variable]

    assert result == expected
    
    
def test_getNonExistingEnv(): 

    variable = "FATHOM_CONFIG_TEST"
    expected = f"Environment variable '{variable}' not found"

    try:
        print("getting result")
        result = config._getEnv(variable)
    except Exception as e:
        print("handling exception")
        result = e
    
    assert str(result) == expected


def test_getOAuthRefreshUrl():

    expected = "https://login.microsoftonline.com/a69c8df4-e648-4b0a-beb9-b3716a01f60e/oauth2/token"
    result = config.getOAuthRefreshUrl()

    assert result == expected  


def test_getStorageAccount():

    expected = "abfss://datalake@datalakegeneva.dfs.core.windows.net/"
    result = config.getStorageAccount()

    assert result == expected  


# def test_getEnvironment():

#     return config._getEnv("ENVIRONMENT")


# def test_getAzureADId():

#     return _getEnv("AZUREADID")


# def test_getAutomationScope():

#     return _getEnv("AUTOMATIONSCOPE")


# def test_getDataLakeStorageType(): 

#     return _getEnv("DATALAKESTORAGE") 


# def test_getResourceGroup(): 

#     return _getEnv("RESOURCEGROUP") 


# def test_getSubscriptionId(): 

#     return _getEnv("SUBSCRIPTIONID") 


# def stripMargin(text):

#     return re.sub('\n[ \t]*\|', '\n', text)


# def help():

#       return f"""
#       <p>Configuration:</p>
#       <table>
#       <tr><th align='left'>Function          </th><th align='left'> Value               </td></tr>
#       <tr><td>getEnvironment()               </td><td> {getEnvironment()}               </td></tr>
#       <tr><td>getStorageAccount()            </td><td> {getStorageAccount()}            </td></tr>
#       <tr><td>getDataLakeStorageType()       </td><td> {getDataLakeStorageType()}       </td></tr>
#       <tr><td>getAutomationScope()           </td><td> {getAutomationScope()}           </td></tr>
#       <tr><td>getResourceGroup()             </td><td> {getResourceGroup()}             </td></tr>
#       <tr><td>getAzureADId()                 </td><td> {getAzureADId()}                 </td></tr>
#       <tr><td>getSubscriptionId()            </td><td> {getSubscriptionId()}            </td></tr>
#       <tr><td>getOAuthRefreshUrl()           </td><td> {getOAuthRefreshUrl()}           </td></tr>
#       <tr><td>getServicePrincipalId()        </td><td> {getServicePrincipalId()}        </td></tr>
#       <tr><td>getServiceObjectId()           </td><td> {getServiceObjectId()}           </td></tr>
#       <tr><td>getServiceCredential()         </td><td> {getServiceCredential()}         </td></tr>
#       <tr><td>getDatalakeConnectionString()  </td><td> {getDatalakeConnectionString()}  </td></tr>
#       </table>
#       """
