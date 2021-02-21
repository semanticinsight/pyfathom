
import fathom.Configuration as config
import os


def test_get_env(): 

    variable = "FATHOM_CONFIG_TEST"
    expected = "1"
    os.environ[variable] = expected

    result = config._get_env(variable)
    
    del os.environ[variable]

    assert result == expected
    
    
def test_get_non_existing_env(): 

    variable = "FATHOM_CONFIG_TEST"
    expected = f"Environment variable '{variable}' not found"

    try:
        print("getting result")
        result = config._get_env(variable)
    except Exception as e:
        print("handling exception")
        result = e
    
    assert str(result) == expected

def test_getOAuthRefreshUrl():

    expected = "https://login.microsoftonline.com/149ec02b-dd91-4520-865e-c116832e8b64/oauth2/token"
    result = config.get_oauth_refresh_url()

    assert result == expected  


def test_get_storage_account():

    expected = "abfss://dataplatform@datalakehousedev.dfs.core.windows.net/"
    result = config.get_storage_account()

    assert result == expected  
