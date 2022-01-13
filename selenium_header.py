from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#headless, start-maximzed, window-size somehow fixed element not interable problem!
options.add_argument('--headless')
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
chrome = webdriver.Chrome(executable_path= "YOUR PATH TO CHROMEDRIVER.EXE", options = options)
