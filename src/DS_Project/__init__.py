#Import Required Modules
import os 
import sys
import logging

#Defining the Log Format
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Creating a Log Directory and File Path
log_dir="logs"
log_filepath =os.path.join(log_dir,"logging.log")
os.makedirs(log_dir, exist_ok=True)

#Configuring the Logging System
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

#Creating a Logger Object
logger=logging.getLogger("datasciencelogger")