import logging

import datetime

import os, sys

class StartLogging():
    def __init__(self, Mode: str = "stdout"):
        LoggingStartTime = datetime.datetime.now()
        formatted_time = LoggingStartTime.strftime("%Y-%m-%d_%H-%M-%S")

        if Mode == "stdout":
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        
        if Mode == "file":
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename=f"{os.path.join(sys.path[0]) + "\\..\\logs\\"}{formatted_time}.log", filemode="a")