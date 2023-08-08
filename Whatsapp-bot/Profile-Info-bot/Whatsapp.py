from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

try:
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the WhatsApp Web URL
    driver.get("https://web.whatsapp.com/")

    # Prompt the user to scan the QR code manually
    print("Scan QR Code")

    # Wait for the user to scan the QR code manually for 60 seconds
    time.sleep(60)

    print("Enter name of person")
    person = input()
    time.sleep(2)
    # XPath for the search input field
    inp_xpath_search = "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']"
    search_input = driver.find_element(By.XPATH, inp_xpath_search)

    # Set the value and trigger events
    search_input.clear()
    search_input.send_keys(person)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Click on the user profile
    profile = driver.find_element(By.XPATH, "//div[@class='_2au8k']")
    profile.click()
    time.sleep(10)

    # Get the page source and parse it using BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Find the container element
    container = soup.find(
        "div", {"class": "lhggkp7q qq0sjtgm ebjesfe0 jxacihee tkdu00h0"}
    )

    # Find and print the user's name
    name = container.find("h2")
    print("User's Name:", name.text)

    # Find and print the user's number
    number = container.find("div", {"class": "a4ywakfo qt60bha0"})
    print("User's Number:", number.text)

    # Find and print the top groups the user is in, if any
    groups = container.find("div", {"class": "_3YS_f _2A1R8"})
    if groups is not None:
        print("Top Groups:")
        group = []
        for items in groups:
            group.append(items.find("div", {"class": "y_sn4"}).text)
        print(group)
    else:
        print("No group's in common")

    # Find and print any common interests or details
    about = container.find(
        "span", {"class": "cw3vfol9 _11JPr selectable-text copyable-text"}
    )
    if about:
        print("About:", about.text)
    else:
        print("No About")

    # Close the WebDriver
    driver.quit()
except Exception as e:
    print("Exception Occured:", e)
