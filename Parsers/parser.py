from typing import Dict
from Locators.page_locators import PageLocators,CardLocators
from selenium.webdriver.common.by import By
import json
import logging

class Parser:
    def __init__(self,parent):
        self.parent = parent

    def jsonUpdate(self,subject_dict : str,subjectName : str) -> Dict:
        """
        This function helps to grab the new announcements and return it to the caller function.
        """
        logging.info("Subjects' JSON File is being updated")
        #0 is the number of announcement, since it's initialization phase, we initialise it with 0
        if subjectName not in subject_dict:
            logging.info(f"{subjectName} is not found in the JSON, it's being initialized.")
            subject_dict[subjectName] = {"numberOfOld": 0,
                                         "numberOfNew": 0,
                                        "announcements" : []  
                                        }

        existingAnnounce = subject_dict[subjectName]["numberOfOld"]
        cardOfAnnouncements = self.parent.find_elements(By.CSS_SELECTOR,PageLocators.CARD_ANNOUNCEMENT)[1:]
        newAnnouncements = (len(cardOfAnnouncements) - existingAnnounce)    
        announcements =  subject_dict[subjectName]["announcements"]
    
        if newAnnouncements:
            logging.info("New announcements are getting updated to the JSON object.")
            for i in cardOfAnnouncements[newAnnouncements-1::-1]:
                announcementTitle = i.find_element(By.CSS_SELECTOR,CardLocators.TITLE).text
                announcementAuthor = i.find_element(By.CSS_SELECTOR,CardLocators.AUTHOR).text
                announcementTask = i.find_element(By.CSS_SELECTOR,CardLocators.TASK).text
                announcements.append(f"Title:\n{announcementTitle}\n\n{announcementAuthor}\n\nAnnouncement:\n{announcementTask}")
                        
        subject_dict[subjectName] = {
            "numberOfOld" : existingAnnounce+newAnnouncements,
            "numberOfNew" : newAnnouncements,
            "announcements" : announcements
        }

        return subject_dict


    def announcementChecker(self,subjectName : str) -> Dict:
        """
        This function loads the subject's announcements(OLD) from the JSON, and get the update it with the new one.
        """
        with open("json\\subject_infos","r") as json_file:
            logging.info("subject_infos JSON file is being read.")
            subject = json.load(json_file)

        new_sub_dict = self.jsonUpdate(subject,subjectName)
        
        with open("json\\subject_infos","w") as json_file:
            logging.info("subject_infos JSON file is being written.")
            json.dump(new_sub_dict,json_file)
        
        return new_sub_dict

            
        


