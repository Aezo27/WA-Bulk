# Python Automated Bulk WhatsApp Messages

It is a python script that sends WhatsApp message automatically from WhatsApp web application. It can be configured to send advertising messages to customers. It read data from an excel sheet and send a configured message to people.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone (You can use bulk contact number saving procedure of email). There is a way without saving the contact number but has the limitation to send the attachment.
* Python 3.8: Download it from https://www.python.org/downloads
* Google Chrome : Download it from https://www.google.com/chrome
* Selenium Web Driver: must be a same version with Google Chrome, you can download it https://chromedriver.chromium.org/downloads
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Selenium: Run in command prompt **pip install selenium** 
* Openpyxl: Run in command prompt **pip install openpyxl**
* Request: Run in command prompt **pip install requests**

## Approach
* User scans web QR code to log in into the WhatsApp web application.
* The script reads a customized message from excel sheet.
* The script reads rows one by one and searches that contact number in the web search box if the contact number found on WhatsApp then it will send a configured message otherwise It reads next row. 
* Loop execute until and unless all rows complete.

Note: If you wish to send an image instead of text you can write attachment selection python code.