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
level=13

# Initialize the Chrome Driver
driver = uc.Chrome()
actions = ActionChains(driver)
# Open the website
driver.get("https://neal.fun/not-a-robot/")
driver.maximize_window()
time.sleep(1)  # Wait for the page to load
#Level 1
driver.find_element(By.CLASS_NAME, "recaptcha-container").click()
time.sleep(2)  
# Set a single item
driver.execute_script(f"window.localStorage.setItem('not-a-robot-level', {level-1});")
driver.execute_script("location.reload()")
time.sleep(1)  # Wait for the page to load

#Level Code Here
srcs = [
"https://neal.fun/not-a-robot/muffins/chihuahuas/1.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/4.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/2.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/5.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/6.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/3.webp"
]
for i in range(1, 17):
    if driver.find_element(By.XPATH,f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]/img').get_attribute("src") in srcs:
        driver.find_element(By.XPATH,f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click() 
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
