import json
from Locators.general_locators import GeneralLocators
from Locators.page_locators import PageLocators
from Parsers.parser import Parser
from typing import Generator, List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import logging

class Page:
    def __init__(self,page):
        self.page = page
        self.page.get("https://mmls2.mmu.edu.my/")

    def _getIdPw(self) -> List:
        """
        This function essentially asks for username and password, if it isn't exist in the json file.
        """
        has_info = False
        with open("json\\randomtextfile","r") as json_file:
            userinfo = json.load(json_file)
            logging.info("Retrieved user information from JSON and checking if it's empty.")
            if userinfo["username"] and userinfo["password"]:
                has_info = True
            
            
        if not has_info:
            userinfo ={ "username" : input("Please enter your student ID: "),
            "password" : input("Please enter your password: ")}
            logging.info("Asking user for ID and Password, and it's being updated to JSON.")
            with open("json\\randomtextfile","w") as json_file:
                json.dump(userinfo,json_file)
        
        return [userinfo["username"],userinfo["password"]]

    def isElementPresent(self,locator):
        try:
            logging.info(f"Checking if \"{locator}\" present.")
            self.page.find_element_by_css_selector(locator)
            return True
        except:
            return False

    def _login(self):
        loginSuccessful = False
        while not loginSuccessful:
            username,password = self._getIdPw()
            username_login = self.page.find_element(By.CSS_SELECTOR,GeneralLocators.LOGIN_ID)
            userpw_login = self.page.find_element(By.CSS_SELECTOR,GeneralLocators.LOGIN_PASSWORD)
        
            username_login.send_keys(username)
            userpw_login.send_keys(password)
            userpw_login.send_keys(Keys.ENTER)
            logging.info("Selenium is attempting to login using user information provided.")

            try:
                WebDriverWait(self.page,3).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR,GeneralLocators.SUBJECT_CARD)
                    )
                )
                loginSuccessful = True
            except:
                loginSuccessful = False
                if self.isElementPresent(GeneralLocators.INVALID_LOGIN):
                    logging.info("Login unsucessful! Reinitializing username and password, reask from user.")
                    print("Invalid Credential!")
                    with open("json\\randomtextfile","w") as json_file:
                        userinfo = {"username":"","password":""}
                        json.dump(userinfo,json_file)



            



    @property
    def _subjectGetter(self) -> Generator:
        logging.info("Getting all the subject cards as an element tag.")
        subject_cards = GeneralLocators.SUBJECT_CARD
        card_list = self.page.find_elements(By.CSS_SELECTOR,subject_cards)
        return card_list

    def view_all_new(self,announcements,subjects):
        logging.info("Viewing all new announcements from all subjects.")
        for i in subjects:
            print(i)
            print("----------------------")
            numberOfNew = announcements[i]["numberOfNew"]
            print(f"New Announcements: {numberOfNew}\n")

            announcements_list = announcements[i]["announcements"]
            print("\n-----------\n"+"\n-----------\n".join([announcements_list[x] for x in range(len(announcements_list)-1,(len(announcements_list)-numberOfNew)-1,-1)])+"\n-----------\n")


    def view_new_announcements(self,announcements,subjectName,all_or_new):
        logging.info(f"Viewing announcements from {subjectName}.")
        print(subjectName)
        if all_or_new == "a":
            print("\n-----------\n"+"\n-----------\n".join([i for i in announcements[subjectName]["announcements"]])+"\n-----------\n")
            
        else:
            numberOfNew = announcements[subjectName]["numberOfNew"]
            if numberOfNew == 0:
                print("\nThere are no new announcements!\n")
            announcements_list = announcements[subjectName]["announcements"]
            print("\n-----------\n"+"\n-----------\n".join([announcements_list[x] for x in range(len(announcements_list)-1,(len(announcements_list)-numberOfNew)-1,-1)])+"\n-----------\n")
            

    def select_subject(self,announcements,subjects):
        logging.info("Selecting subject to be view.")
        for i,j in enumerate(subjects):
            print(f"{i+1} : {j}")
            print("-----------")
        subjectID = 0
        subjectID_set = {i+1 for i in range(len(subjects))}
        while subjectID not in subjectID_set:
            subjectID = int(input("Please select the ID of the subject that you would like to view\n---->"))
        
        all_or_new = 0
        all_or_new_set = {"a","n"}
        while all_or_new not in all_or_new_set:
            all_or_new = input("A - All Announcements\nN - New Announcements Only\n---->").lower()
            if all_or_new in all_or_new_set:
                print("\n")
            else:
                print("Invalid input")

        
        #-1 in the index of subejcts because we have added 1 to each of the index, in the last operation
        self.view_new_announcements(announcements,subjects[subjectID-1],all_or_new)



    def subjects_checker(self):
        subjects = []
        for i in range(len(self._subjectGetter)):
            #rerendering 
            element = self._subjectGetter[i]
            #i.text somehow return the name of the subject without having you find it again with css selector
            subjectName = element.text
            logging.info(f"{subjectName} is being checked for new announcements.")
            subjects.append(subjectName)
            element.click()
            new_announcements = Parser(self.page).announcementChecker(subjectName)

            #back to home page, to select the next subject card
            home_button = self.page.find_element(By.CSS_SELECTOR,PageLocators.HOME_BUTTON)
            home_button.click()

        print("Announcements\n------------------------")
        for i in subjects:
            subjectName = i
            numberofNew = new_announcements[i]["numberOfNew"]
            print(f"{subjectName}\nNew Announcements: {numberofNew}\n")
        
        options = 0
        #a random value , so that the while loop recognize "options"
        options_set = {1,2,3}
        while True:
            while options not in options_set:
                logging.info("Asking for user options for viewing announcements.")
                options = int(input("1.View all new announcements\n2.View by subject\n3.Main Menu\n---Please Select The Number--->"))
                if options not in options_set:
                    print("Invalid Option Selected")
            if options == 1:
                self.view_all_new(new_announcements,subjects)
            elif options == 2:
                self.select_subject(new_announcements,subjects)
            else:
                break
            options = 0

            




            


            


        





