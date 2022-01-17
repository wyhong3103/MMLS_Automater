from typing import List
import cv2
import pyautogui
from pyzbar import pyzbar
import time
import os
import json
from selenium.common.exceptions import TimeoutException
from Locators.attendance_locators import AttendanceLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
import re


class noQrCodeFound(ValueError):
    pass

class AttendancePage:
    def __init__(self,parent):
        self.parent = parent
        self.qrcodes = self.qrcode_read
        if self.qrcodes:
            for i,j in enumerate(self.qrcodes):
                url = j
                pattern = "https://mmls2.mmu.edu.my/attendance.+"
                logging.info("Using regular expression to validate the link provided.")
                if re.search(pattern,url):
                    if self.parent.current_url == "https://mmls2.mmu.edu.my/attendance/success/home":
                        home_button = self.parent.find_element(By.CSS_SELECTOR,AttendanceLocators.HOME_BUTTON)
                        home_button.click()
                    self.parent.get(j)
                    logging.info("Accessing to the attendance site.")
                    print(f"QR Code {i+1}:")
                    self.take_attendance()
                else:
                    logging.info("QR Code contains non-mmls link.")
                    print(f"QR Code {i+1}:")
                    print("QR Code contains non-mmls link.\n")


    @property
    def qrcode_read(self):
        """
        This function convert the QR Code on your screen to URL, and return it.
        """
        try:
            logging.info("Preparing to scan QR Code.")
            for i in range(5,0,-1):
                print(f"Make sure the qrcode is staying on your screen... {i}")
                time.sleep(1)
            screenshot = pyautogui.screenshot()
            logging.info("QRCode.jpg is being saved, and waiting to be scan.")
            screenshot.save("qrcode.jpg")
            img = cv2.imread("qrcode.jpg")
            logging.info("QRCode is scanned and decoded into strings.")
            qrcode = pyzbar.decode(img)
            #detect and decode returns a few argument, the first is what you want, the string
            qrcodes = []
            for qr in qrcode:
                qrcodes.append(qr.data.decode("utf-8"))
            os.remove("qrcode.jpg")
            logging.info("QRCode.jpg is removed and deleted from the machine.")
            if not qrcodes:
                raise noQrCodeFound
            return qrcodes
        except noQrCodeFound:
            logging.info("QR code is not detected!")
            print("\nQR code is not found on the screen!\n")
            return False

    def getIdPw(self) -> List:
        """
        This function essentially asks for username and password, if it isn't exist in the json file.
        """
        has_info = False
        with open("json\\randomtextfile","r") as json_file:
            logging.info("Retrieving User Information from JSON file, and checking whether it's empty.")
            userinfo = json.load(json_file)
            if userinfo["username"] and userinfo["password"]:
                has_info = True
            
        if not has_info:
            logging.info("User information is empty in the JSON File, Interpreter is asking for it.")
            userinfo ={ "username" : input("Please enter your student ID: "),
            "password" : input("Please enter your password: ")}
            with open("json\\randomtextfile","w") as json_file:
                json.dump(userinfo,json_file)
            logging.info("User Information is being updated to the JSON File.")
        
        return [userinfo["username"],userinfo["password"]]

    def take_attendance(self):
        """
        This function login to the site and take attendance for you.
        """
        login_successful = False
        while not login_successful:
            usernameInput = self.parent.find_element(By.CSS_SELECTOR,AttendanceLocators.USERNAME)
            pwInput = self.parent.find_element(By.CSS_SELECTOR,AttendanceLocators.PASSWORD)
            
            username,password = self.getIdPw()
            
            usernameInput.send_keys(username)
            pwInput.send_keys(password)
            pwInput.send_keys(Keys.ENTER)
            logging.info("Selenium is attempting to login with the user information provided from JSON.")

            try:
                WebDriverWait(self.parent,3).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR,AttendanceLocators.HOME_BUTTON)
                    )
                )
                login_successful = True
            except TimeoutException:
                logging.info("TimeoutException is raised, it's either of the slow connection or login unsucessful.")
                if self.parent.current_url != "https://mmls2.mmu.edu.my/attendance/success/home":
                    logging.info("Login Unsucessful, invalid credential.")
                    login_successful = False
                    print("\nInvalid Credential!\n")
                    with open("json\\randomtextfile","w") as json_file:
                            userinfo = {"username":"","password":""}
                            json.dump(userinfo,json_file)
                    logging.info("Reinitialized the user information in JSON file. Will be asking for it again.")
        #print message
        logging.info("Login successfully and taking attendance...")
        message = self.parent.find_element(By.CSS_SELECTOR,AttendanceLocators.MESSAGE).text
        logging.info(f"Browser : {message}")
        print(f"\n{message}\n")
        






    
        


