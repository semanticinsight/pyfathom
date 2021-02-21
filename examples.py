# create a session scope connection using a key vault secured
# security principal credentials
from fathom.ConnectStorage import connect_storage
connect_storage()

# load up the configuration and see what there is
from fathom.Configuration import help
help()


