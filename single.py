from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import math
# Set the desired level here
level=16

# Initialize the Chrome Driver
driver = webdriver.Chrome()
actions = ActionChains(driver)
# Open the website
driver.get("https://neal.fun/not-a-robot/")
driver.maximize_window()
time.sleep(1)  # Wait for the page to load
#Level 1
driver.find_element(By.CLASS_NAME, "recaptcha-container").click()
# Set a single item
driver.execute_script(f"window.localStorage.setItem('not-a-robot-level', {level-1});")
driver.execute_script("location.reload()")
time.sleep(1)  # Wait for the page to load

#Level Code Here
