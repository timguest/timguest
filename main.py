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



url = "https://qsf-acc.dss-d.pwcinternal.com/handles/qsf-handle-chapter-x-impact?tab=input"
email = "tim.gast@pwc.com"
json_file_path = '/Users/tgast004/Pycharmprojects/timguest/form_chapx.json'
json_file_path2 = '/Users/tgast004/Pycharmprojects/timguest/form_work.json'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
email_input = driver.find_element(By.ID, "initEmail")
email_input.send_keys(email)
time.sleep(1)
next_button = driver.find_element(By.XPATH, '//button[text()="Next"]')
next_button.click()
time.sleep(9)

file_input = driver.find_element(By.XPATH, "//input[@type='file']")
driver.execute_script("arguments[0].style.display = 'block';", file_input)
file_input.send_keys(json_file_path)
time.sleep(2)
submit_button = driver.find_element(By.XPATH, '//button[@type="button" and @class="a-btn a-btn-primary a-btn-sm sc-fvNpTx gRTjlJ a-keyboard-hover-only-div" and contains(text(), "Submit")]')
submit_button.click()

time.sleep(4)

new_url = 'https://qsf-acc.dss-d.pwcinternal.com/handles/qsf-handle-work-resumption-fund?tab=input'
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
driver.get(new_url)
time.sleep(4)

file_input2 = driver.find_element(By.XPATH, "//input[@type='file']")
driver.execute_script("arguments[0].style.display = 'block';", file_input2)
file_input2.send_keys(json_file_path2)
print('succes')
time.sleep(2)
# submit_button = driver.find_element(By.XPATH, '//button[@type="button" and @class="a-btn a-btn-primary a-btn-sm sc-fvNpTx gRTjlJ a-keyboard-hover-only-div" and contains(text(), "Submit")]')
submit_button = driver.find_element(By.XPATH, '//button[@type="button" and contains(@class, "a-btn-primary") and contains(text(), "Submit")]')
submit_button.click()
time.sleep(10)

#
#
# #
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Start a new instance of the Firefox driver
# driver = webdriver.Chrome()
#
# # Navigate to the website
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("https://tickets.feyenoord.nl/events/home/Feyenoord-RKC_Waalwijk")
#
# time.sleep(10)
# # Define the class name you're looking for
#
# # Define a wait time to give the page time to load before checking for the class
# xpath = 'K'
#
# # Define a wait time to give the page time to load before checking for the element
# wait_time = 3
#
# while True:
#     try:
#         # Wait for the element to be available on the page
#         button_element_identifier = "K"
#
#         # Wait for the button to be available
#         button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, button_element_identifier))
#         )
#
#         # If the class is available, click on it
#         button.click()
#
#         from selenium.webdriver.common.action_chains import ActionChains
#
#         try:
#             xpath = '//*[@data-id="16065795"]'
#             element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
#             driver.execute_script(
#                 "var evt = new MouseEvent('click', {bubbles: true, cancelable: true, view: window}); arguments[0].dispatchEvent(evt);",
#                 element)
#         except Exception as e:
#             print(f"Error: {e}")
#             driver.quit()
#
#         time.sleep(10)
#
#         break
#     except:
#         # If the class is not available, refresh the page and try again
#         driver.refresh()
#
# # Close the browser
# driver.quit()
