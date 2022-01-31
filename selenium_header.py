from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#headless, start-maximzed, window-size somehow fixed element not interactable problem!
options.add_argument('--headless')
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
#binary_location helps to fix some of the bugs, so I decided to add it here for safety reasons
options.binary_location = "YOUR PATH TO YOUR CHROME BROWSER"
chrome = webdriver.Chrome(executable_path= "YOUR PATH TO CHROMEDRIVER.EXE", options = options)
