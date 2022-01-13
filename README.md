# MMLS Automator 2.0 (I guess, fixed a few bugs)
This python application let you automate stuff like taking attendance during your lecture , check your MMLS for any new announcements.
<br>
Inspiration : MMLS2 is suck, no notification from lecturers, QR code is unscannable using MMLS mobile application, that's what inspire me to build this.

## Instructions
1.First , pip install these few stuff (Make sure your python is added to path)
<br>
-pip install opencv-python
<br>
-pip install selenium
<br>
-pip install pyautogui
<br>
-pip install pyzbar
<br>
2.Download chromedriver.exe from https://chromedriver.chromium.org/downloads, make sure you downloaded the right version for your browser, and also include the path to it in selenium_header.py (check out the file , and you will see where should you put it on), also the path of your chrome.exe.
<br>
3.Run app.py to start this application.
<br>
Other libraries are included in python itself (Probably).
<br>
There's no GUI for this application, all things are done in text-based UI. But it's still user-friendly though, feel free to use it. :))

## Functionalities
-View annnouncements from MMLS
<br>
-Take attendance from QR Code, (it would also works in a case where you got two QR code on the screen)
<br>
And that's essentially what it does.

## Modules Included
-OpenCV (Image processing , i guess)
<br>
-Selenium (Browser Automation)
<br>
-Logging (Logging)
<br>
-Datetime (Use for date and time)
<br>
-PyAutoGui (Screenshot and saving it)
<br>
-OS (Deleting the screenshot of QR Code after saving it)
<br>
-Json(Use to store files, like announcements, user information)
<br>
-Time(Countdown timer)
<br>
-Pyzbar (QR Code decode)
<br>
-Regular Expression (Filter the links)

## Side Note
Username and password stored are not encrypted and all, so please, be aware of it, and use it on your own risk.

## Thoughts
It was a pretty fun project to do, it's been sometimes since the last time I dealt with selenium and other modules. Not sure how can we implement asyncIO in this application, but I am pretty sure this application can still be optimize and all.

## Bugs
-Did not found any of them yet, in 2.0

## What's coming next??
-Most probably, a GUI version of this thing.
<br>
-I am collaborating with my dude @goldensquirell to improve it
<br>
-Who knows...

## QnA
Selenium gives "selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary", what do I do?
<br>
https://stackoverflow.com/questions/46026987/selenium-gives-selenium-common-exceptions-webdriverexception-message-unknown

### HAVE FUN USING IT.
