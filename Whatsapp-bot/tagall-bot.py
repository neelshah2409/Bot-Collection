#IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code manually
time.sleep(10)

# Find the group name element
group_name = driver.find_element_by_xpath("//span[@title='Group Name']")    # Replace Group Name with the name of your group
group_name.click()

# Find the message box
message_box = driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']")
message_box.click()

# Type the message
message_box.send_keys("@everyone")

# Send the message
send_button = driver.find_element_by_xpath("//button[@class='_35EW6']")
send_button.click()

# Close the browser
driver.close()
