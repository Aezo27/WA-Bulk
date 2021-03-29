# Program to send bulk customized message through WhatsApp web application
# Author @inforkgodara
# Modifier @Aezo27

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas
import time
import requests
import datetime

# Load the chrome driver
driver = webdriver.Chrome()

# Open WhatsApp URL in chrome browser
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

# Get ada from the api
response = requests.get('http://127.0.0.1:8000/api/whatsapp')
json = response.json()

# Iterate data from api till to finish
for data in json:
    now = datetime.datetime.now().strftime('%H:%M')
    time = data['time']
    if now > time:
        if (data['status'] == 0):
            # Assign customized message
            pesan = "Halo {nama}, Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

            # Locate search box through x_path
            search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
            person_title = wait.until(lambda driver:driver.find_element_by_xpath(search_box))

            # Clear search box if any contact number is written in it
            person_title.clear()

            # Send contact number in search box
            person_title.send_keys(str(data['nomor']))

            # Wait for 5 seconds to search contact number
            time.sleep(2)

            try:
                # Load error message in case unavailability of contact number
                element = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
            except NoSuchElementException:
                # Format the message
                pesan = pesan.replace('{nama}', data['nama'])
                person_title.send_keys(Keys.ENTER)
                actions = ActionChains(driver)
                actions.send_keys(pesan)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                requests.put("http://127.0.0.1:8000/api/update-whatsapp",
                            data={'id': data['id'], 'stts': '1'})

# Close chrome browser
# driver.quit()
