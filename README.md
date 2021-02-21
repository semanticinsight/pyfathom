<img src="https://img.shields.io/badge/Python-v3.7-blue">

# Introduction 
Python framework for databricks. A library that handles the following either clusterside of locally (using Databricks-Connect):
- Environment Configuration
- Logging
- Azure Storage Session Connection

## Examples:

see examples.py.

Mount azure storage using a session scoped connection and Azure AD service principal backed by scoped secrets and cluster configuration. This is the preferred connection option for automated jobs running under a service principal:

```
from fathom.ConnectStorage import connect_storage
connect_storage()
```

```
Connected:
-----------------------------------------------
 environment = DEV
 storage account = abfss://datalake@datalakegeneva.dfs.core.windows.net/ 
```

Load up the configuration and see what there is:
```
from fathom.Configuration import *
help()
```

```
Configuration:
--------------------------------------------------------
get_environment()           : LOCALDEV 
get_storage_account()       : abfss://dataplatform@datalakehousedev.dfs.core.windows.net/        
get_dataLake_storage_type() : AzureDataLakeGen2     
get_automation_scope()      : kv-datalytics-dev        
get_resource_group()        : databricks-dev          
get_azure_ad_id()           : 149ec02b-dd91-4520-865e-c116832e8b64            
get_subscription_id()       : 2e6423fc-1b92-400c-a10b-9a0c166d97d1          
get_oauth_refresh_url()     : https://login.microsoftonline.com/149ec02b-dd91-4520-865e-c116832e8b64/oauth2/token      
get_service_principal_id()  : 61ac4bea-f0ec-4133-8794-260ad87c4436       
get_service_credential()    : [REDACTED]   
```

# Setup

Create virual environment and install dependencies for local development:

```
python3.7 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev_requirements.txt
```

Comes configured with databricks-connect==7.1.14, see requirements.txt. To use a different version review breaking changes before hand! & delete these lines in requirements.txt.

```
databricks-connect==7.1.14
py4j==0.10.9
six==1.15.0
```

Install your required version:
```
pip install -U databricks-connect==?
pip freeze > requirements.txt
```

## Configure Databricks Connect

Databricks connect **MUST** be the same version as the remote cluster and is not compatible with clusters configured with AD security pass through. It doesn't mean those libraries can't be used on those clusters but does mean those clusters can't be used for interactice development and testing.

Configure databricks connect. Note ensure that you've created a databricks secure token in your own user settings since you'll need it to configure databricks connect:

```
databricks-connect configure
```

Use the following settings:
```
* Databricks Host: https://adb-6566450296336018.18.azuredatabricks.net
* Databricks Token: [your-own-secure-token]
* Cluster ID: 0206-202555-fords669
* Org ID: 6566450296336018
* Port: 15001
```

Test it:
```
databricks-connect test
```

## Configure Databricks Connect DBUtils Token

This library uses DBUtils to pull secrets. To run remotely you need to set a 48hr security token.
Run the following in a notebook on cluster to get your token:
```
displayHTML(
  "<b>Privileged DBUtils token (expires in 48 hours): </b>" +
  dbutils.notebook.getContext.apiToken.get.split("").mkString("<span/>"))
```

Set the token in your local environment:
```
export DBUTILSTOKEN=<YOUR TOKEN VALUE>
```

Or if running on VSCode I recommend adding something like this to your ./.vscode/launch.json

```
    "configurations": [
        
        {
            "name": "Python: Main",
            "type": "python",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "env": { "DBUTILSTOKEN": "YOUR TOKEN VALUE" }
        }
    ]
```


# Build

Build python wheel for Databricks cluster:
```
python setup.py sdist bdist_wheel
```

## Auto-Versioning

Binary versioning is handled using setuptools-git-versioning configured in the setup.py.
The version includes the target databricks runtime version.

Note the following templates - subject to review. Note Azure DevOps requires PEP440 versioned binaries:
```
name=f"pyfathom-{DATABRICKS_RUNTIME}",
version_config={
    "template": "{tag}",
    "dev_template": "{tag}.dev{ccount}",
    "dirty_template": "{tag}.dev{ccount}.git{sha}.dirty",
    "starting_version": "0.0.1",
    "version_callback": None,
    "version_file": None,
    "count_commits_from_version_file": False
}
```

- template - clean build with commits or changes beyond the tag
- dev_template - commits are ahead of the latest version tag
- dirty_template - you have changes beyond the tag and last commits that have not yet been commited, should only ever occur on your local development

e.g. Tagged build examples
```
template: fathom.1-0.1.0-py3-none-any.whl
dev_template: fathom-dbr7.1_0.1.0.dev1-py3-none-any.whl
dirty_template: fathom.1_v0.1.0.dev1_git.74ea7515.dirty-py3-none-any.whl
```

# Test

Note that testing will spin the remote databricks cluster confgured in your databricks connect configuration. If the cluster isn't already running or you're not using cluster pools then testing may be slow on the 1st run. Ensure to review the cluster shut down policy following development testing; **shut it down if necessary**.

**NOTE:** for obvious reasons functions that return secrets using a 48 hr user interactive token cannot be included in the test automation! This is a current limitation of Databricks Connect dbutils. This will affect the amount of test converage that can be achieved.

```
pip install --editable .

pytest
```


