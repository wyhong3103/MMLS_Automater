# MMLS Automator 2.0 

This python application let you automate stuff like taking attendance during your lecture , check your MMLS for any new announcements.

Inspiration : MMLS2 has no notification from lecturers, QR code is unscannable using MMLS mobile application, that's what inspired me to build this.

## Instructions

1. Install a chromium-based browser (Google Chrome, Brave, Chromium, etc.). You can skip this step if you already have one downloaded.

2. pip install these few stuff using (Make sure your python is added to path)

    `$ pip install -r "requirements.txt"`

    (requirements.txt of this directory)

    OR run the following commands in sequence

    `$ pip install opencv-python`

    `$ pip install selenium`

    `$ pip install pyautogui`

    `$ pip install pyzbar`

    `$ pip install pillow`

3. Download [chromedriver.exe](https://chromedriver.chromium.org/downloads), make sure you downloaded the right version for your browser, and also include the path to it in selenium_header.py (check out the file , and you will see where should you put it on), also the path of your chrome.exe.

4. Run `$ py app.py` to start this application.

    Other libraries are included in python itself (Probably).

    There's no GUI for this application, all things are done in text-based UI. But it's still user-friendly though, feel free to use it. :))

## Functionalities

- View announcements from MMLS

- Take attendance from QR Code, (it would also works in a case where you got two QR code on the screen)

And that's essentially what it does.

## Modules Included

- OpenCV (Image processing , i guess)

- Selenium (Browser Automation)

- Logging (Logging)

- Datetime (Use for date and time)

- PyAutoGui (Screenshot and saving it)

- OS (Deleting the screenshot of QR Code after saving it)

- Json(Use to store files, like announcements, user information)

- Time(Countdown timer)

- Pyzbar (QR Code decode)

- Regular Expression (Filter the links)

- Pillow

## Side Note

Username and password stored are not encrypted and all, so please, be aware of it, and use it on your own risk.

## Thoughts

It was a pretty fun project to do, it's been sometimes since the last time I dealt with selenium and other modules. Not sure how can we implement asyncIO in this application, but I am pretty sure this application can still be optimize and all.

## Bugs

- Did not found any of them yet, in 2.0

## What's coming next??

- Most probably, a GUI version of this thing.

- I am collaborating with my dude @goldensquirrel11 to improve it

- Who knows...

## QnA

- *empty for now*

## License & copyright

Licensed under [MIT License](LICENSE)


### HAVE FUN USING IT
