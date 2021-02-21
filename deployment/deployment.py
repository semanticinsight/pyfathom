import os, fnmatch, sys


os.environ["DATABRICKS_API_HOST"] = sys.argv[1]
os.environ["DBUTILSTOKEN"] = sys.argv[2]
print(os.getcwd())

from spores import Workspace, Jobs, DBFS
from uuid import uuid4
from pprint import pprint

build_dir = sys.argv[3]
deploy_dir = sys.argv[4]
filename = sys.argv[5]

wheels = DBFS.find_file('*.whl', build_dir)

for whl in wheels:

    whl_filename = os.path.basename(whl)

    print(f"{whl} => {deploy_dir}/{whl_filename}")
    DBFS.dbfs_upload(whl, f"{deploy_dir}/{whl_filename}", True)