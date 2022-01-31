from menu import menu
from datetime import datetime
import os
import logging

directory_list = os.listdir()
if "logs" not in directory_list:
    logging.info("Creating logs directory")
    os.mkdir("logs")
date = datetime.today().strftime("%d-%m-%y--%I-%M")
logging.basicConfig(format = "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",level = logging.INFO, filename = f"logs\\logs-{date}.txt")

def main():
    logging.info("Starting main menu.")
    menu()
    logging.info("Ending this application.")

if __name__  == "__main__":
    main()
