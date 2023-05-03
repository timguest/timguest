from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://tickets.feyenoord.nl/events/home/Feyenoord-Ajax")
time.sleep(20)

# Define the class name you're looking for
class_name = "section "

# Define a wait time to give the page time to load before checking for the class
wait_time = 3

while True:
    try:
        # Wait for the class to be available on the page
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )

        # If the class is available, click on it
        element.click()
        break
    except:
        # If the class is not available, refresh the page and try again
        driver.refresh()

# Close the browser
driver.quit()
