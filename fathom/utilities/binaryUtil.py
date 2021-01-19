from ..SparkContext import getDbutils
from ..Configuration import getEnvironment


def containsBinary(path:str, containsInName:str):

  _dbutils = getDbutils(getEnvironment())
  listBinaries = _dbutils.fs.ls(path)
  wheels = [i.path for i in listBinaries if name.lower() in i.name.lower()]
  
  if len(binaries) > 0:
    return True
  else:
    return False
  
  
def getBinaryPaths(containsInName:str, rootPath:str="dbfs:/FileStore/jars/"):

  _dbutils = getDbutils(getEnvironment())
  listDirs = _dbutils.fs.ls(rootPath)
  result = [i.path for i in listDirs if containsBinary(i.path, containsInName)]
  
  return result
  
  
def deleteBinaries(containsInName:str):

  _dbutils = getDbutils(getEnvironment())
  listDirs = getBinaryPaths(containsInName)
  result = [_dbutils.fs.rm(i, True) for i in listDirs]
  
  return result