# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver

# Set the path to the ChromeDriver executable

url = "https://qsf-acc.dss-d.pwcinternal.com/handles/qsf-handle-admin-insight?tab=input"
from selenium import webdriver
import time
import os

# Replace with your target URL



timeurl = "https://qsf-acc.dss-d.pwcinternal.com/handles/qsf-handle-chapter-x-impact?tab=input"
email = "tim.gast@pwc.com"
json_file_path = '/Users/tgast004/Pycharmprojects/timguest/form_chapx.json'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
email_input = driver.find_element(By.ID, "initEmail")
email_input.send_keys(email)
time.sleep(1)
next_button = driver.find_element(By.XPATH, '//button[text()="Next"]')
next_button.click()
time.sleep(12)
# Locate and click the upload button with the unique class
upload_button = driver.find_element(By.CLASS_NAME, "icon-upload-outline")  # Replace 'unique-class' with the actual class name
upload_button.click()
time.sleep(5)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Wait for the file input element to become visible
file_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@type="file"]'))
)

# Send the JSON file path to the file input element
file_input.send_keys(os.path.abspath(json_file_path))