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


# Initialize the Chrome Driver
driver = uc.Chrome()


# Open the website
driver.get("https://neal.fun/not-a-robot/")
driver.maximize_window()
time.sleep(1)  # Wait for the page to load
#Level 1
driver.find_element(By.CLASS_NAME, "recaptcha-container").click()
time.sleep(2)  
# Set a single item
driver.execute_script("window.localStorage.setItem('not-a-robot-level', '14');")
driver.execute_script("location.reload()")
time.sleep(1)  # Wait for the page to load

ActionChains(driver).click(driver.find_element(By.XPATH, '//*[@id="park-canvas"]')).perform()

actions = ActionChains(driver)
actions.key_down(Keys.ARROW_UP).perform()
time.sleep(1.65)
actions.key_down(Keys.ARROW_RIGHT).perform()
time.sleep(.5)
actions.key_up(Keys.ARROW_RIGHT).perform()
time.sleep(.7)
actions.key_up(Keys.ARROW_UP).perform()
time.sleep(.5)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(2)
