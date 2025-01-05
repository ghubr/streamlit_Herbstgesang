import os
import sys
# config.py defines location of root directory. Root directory lies one level ABOVE the one config.py is located in
# ROOT_DIR is project directory containing folders src, data, ...

###################################################################################
#
# Set up PROJECT_PATH and working direcoty based on position of config.py
#
###################################################################################
# this works also for scripts under src/snippetes
CUR_DIR = os.path.dirname(os.path.abspath(__file__)) # position of config.py

# CUR_DIR = os.path.abspath(os.getcwd()) # position of config.py

PROJECT_PATH = os.path.dirname(CUR_DIR) # directory above the one config.py lies in
__PROJECT_CONFIG__ = dict() # dictionary to store project configuration data in, e.g. input data file names


###################################################################################
#
# Set working directory
#
####################################################################################
os.chdir(CUR_DIR) # working directory is 'src'

###################################################################################
#
# Modify sys.path so that config files can be import-ed
#
####################################################################################
sys.path.append( os.path.join(PROJECT_PATH, 'src') )
sys.path.append( os.path.join(PROJECT_PATH, 'src', 'oval') )

###################################################################################
#
# Assumed project structure
#
###################################################################################
# PROJECT_PATH
#     src
#       config.py
#       data
#     data
#         raw
#         processed
#     output
#        tmp
#     ...



###################################################################################
#
# Define all project related paths (data, output etc.) relative to PROJECT_PATH
#
###################################################################################
PATHS = dict() # dictionary of global PATHS variables
PATHS['PATHROOT']               = PROJECT_PATH
PATHS['pathToDataRoot']         = os.path.join(PATHS['PATHROOT'], "data")
PATHS['pathToData']             = os.path.join(PATHS['PATHROOT'], "data", "processed") 
PATHS['pathToDataRaw']          = os.path.join(PATHS['PATHROOT'], "data", "raw")
PATHS['pathToDataIntermediate'] = os.path.join(PATHS['PATHROOT'], "data", "intermediate")
PATHS['pathToDataSupp']         = os.path.join(PATHS['PATHROOT'], "data", "supporting")
PATHS['pathToOutput']           = os.path.join(PATHS['PATHROOT'], "output")
PATHS['pathToTmp']              = os.path.join(PATHS['PATHROOT'], "output", "tmp") # new 1.8.23
# check if folders exist
#for f in [PATHS['PATHROOT'], PATHS['pathToDataRaw'], PATHS['pathToData'], PATHS['pathToDataSupp'], PATHS['pathToOutput']]:
for f in PATHS.values():
    if not os.path.exists(f):
        print("WARNING: Folder does not exist:", f)




        
pathToDataRoot           = (PATHS['pathToDataRoot'])
pathToData               = (PATHS['pathToData'])
pathToDataRaw            = (PATHS['pathToDataRaw'])
pathToDataIntermediate   = (PATHS['pathToDataIntermediate'])
pathToDataSupp           = (PATHS['pathToDataSupp'])
pathToOutput             = (PATHS['pathToOutput'])
pathToTmp                = (PATHS['pathToTmp']) # new 1.8.23

###################################################################################
        
GLOB = dict() # dictionary of global variables





###################################################################################
#OVERRIDES the old string definitions. Use resolve

from pathlib import Path
PATHROOT = Path(PROJECT_PATH)     
pathToDataRoot           = PATHROOT / 'data'
pathToData               = PATHROOT / 'data' / 'processed'
pathToDataRaw            = PATHROOT / 'data' / 'raw'
pathToDataIntermediate   = PATHROOT / 'data' / 'intermediate'
pathToDataSupp           = PATHROOT / 'data' / 'supporting'
pathToOutput             = PATHROOT / 'output'
pathToTmp                = PATHROOT / 'output' / 'tmp'


###################################################################################
# CHANGELOG #######################################################################
# 2021-01-13 Pathlib added

if __name__=="__main__":
    print(f"Current working directory is now \"{os.getcwd()}\".")
    

# following convention should be followed
# fp = full path, e.g. C:\foo\bar\dummy.txt
# fn = file name, e.g. dummy.txt
# fdir = directory, e.g. C:\foo\bar