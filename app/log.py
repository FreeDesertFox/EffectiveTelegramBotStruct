import logging

import datetime

import os, sys

class StartLogging():
    def __init__(self, Mode: str = "console"):
        LoggingStartTime = datetime.datetime.now()
        FormatedDate = LoggingStartTime.strftime("%Y-%m-%d_%H-%M-%S")

        LogPath = os.path.join(sys.path[0]) + "/../logs/"

        if Mode == "console":
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        
        if Mode == "file":
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename=f"{LogPath}{FormatedDate}.log", filemode="a")