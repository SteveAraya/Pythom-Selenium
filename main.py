# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)
url = "https://practicetestautomation.com/practice-test-login/"

driver.get(url)

username_locator = driver.find_element(By.ID, "username")
password_locator = driver.find_element(By.ID, "password")
submit_btn_locator = driver.find_element(By.ID, "submit")

username_locator.send_keys("student")
password_locator.send_keys("Password123")
submit_btn_locator.click()
time.sleep(2)

actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

log_out_btn_location = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_btn_location.is_displayed()

driver.close()
