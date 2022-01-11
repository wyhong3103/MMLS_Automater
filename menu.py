from selenium_header import *
from Pages.page import Page
from Pages.attendance import AttendancePage
import logging

def menu():
    logging.info("Main menu started.")
    print(f"MMLS Automation 1.0")
    options_set = {"M","A","E"}
    options = 0

    while options not in options_set:
        options = input("M - Check MMLS' Announcement\nA - Take Attendance\nE - Exit\n---->").capitalize()
        logging.info(f"Option {options} is selected.")
        if options == "M":
            logging.info(f"Creating MMLS' Instance.")
            mmls = Page(chrome)
            logging.info(f"Attempting to Login.")
            mmls._login()
            logging.info(f"Login Successfully, and now starting to do announcement checking.")
            mmls.subjects_checker()
        elif options == "A":
            logging.info(f"Attendance Instance is created.")
            AttendancePage(chrome)
        elif options == "E":
            logging.info(f"Closing chrome browser.")
            chrome.close()
            print("Thanks for using this application!")
            break
        else:
            logging.info(f"Invalid option selected, main menu.")
            print("Invalid option!")
        logging.info("Option is being reinitialized to 0.")
        options = 0
            
