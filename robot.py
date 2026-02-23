from asyncio import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import math

# Initialize the Chrome Driver
driver = webdriver.Chrome()
actions = ActionChains(driver)

    # Open the website
driver.get("https://neal.fun/not-a-robot/")
driver.maximize_window()
time.sleep(1)  # Wait for the page to load

#Level 1
driver.find_element(By.CLASS_NAME, "recaptcha-container").click()
time.sleep(2)  

#Level 2
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[3]").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[4]").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[7]").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]").click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1) 

#Level 3
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="2":
    driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div").click()
    driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/div/input").send_keys("YHRPCD")
    driver.find_element(By.XPATH,"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/button").click()
time.sleep(1)  

#Level 4
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[2]/img").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[3]/img").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[6]/img").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]/img").click()
driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[9]/img").click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 5
for i in range(1, 10):
    #click each item until its style attribute contains "rotate(360deg)"
    while "rotate(360deg)" not in driver.find_element(By.XPATH, f"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div[{i}]").get_attribute("style"):
        driver.find_element(By.XPATH, f"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div[{i}]").click()
        time.sleep(0.1)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 6
targets = [
    (By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div"),
    (By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div"),
    (By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div"),
    (By.ID, "captcha-verify-button"),
    (By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/img")
]

while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');") == "5":
    for selector, value in targets:
        try:
            driver.find_element(selector, value).click()
        except (NoSuchElementException, ElementClickInterceptedException):
            # If a specific line fails, it just skips to the next target in the list
            continue
time.sleep(1)
# level 7
full_list = []
clicked_elements = set()

for i in range(1, 91):
    xpath = f'//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]/div'
    try:
        element = driver.find_element(By.XPATH, xpath)
        full_list.append({"text": element.text.strip().upper(), "el": element})
    except Exception:
        full_list.append({"text": "?", "el": None})

grid = [full_list[i:i + 10] for i in range(0, 90, 10)]
rows, cols = 9, 10

def find_and_click(target, grid):
    target = target.upper()
    rev_target = target[::-1]
    n = len(target)
    
    for r in range(rows):
        for c in range(cols):
            directions = [
                (0, 1),   # Horizontal
                (1, 0),   # Vertical
                (1, 1),   # Diagonal Down-Right
                (-1, 1)   # Diagonal Up-Right
            ]

            for dr, dc in directions:
                end_r = r + dr * (n - 1)
                end_c = c + dc * (n - 1)
                
                if 0 <= end_r < rows and 0 <= end_c < cols:
                    seg = [grid[r + i * dr][c + i * dc] for i in range(n)]
                    word = "".join([s["text"] for s in seg])
                    
                    if word == target or word == rev_target:
                        for s in seg:
                            if s["el"] and s["el"].id not in clicked_elements:
                                s["el"].click()
                                clicked_elements.add(s["el"].id)
                                time.sleep(0.1)
                        return

for word in ["STOPSIGN", "BIKE"]:
    find_and_click(word, grid)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

# level 8
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="7":
    driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div").click()
    driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/div/input").send_keys("2042 GP J")
    driver.find_element(By.XPATH,"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/button").click()
time.sleep(1)  

# level 9
driver.find_element(By.XPATH,"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[2]/div/div/div").click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[2]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[4]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[4]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[4]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div[4]/div[4]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[2]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[2]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div[4]').click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div/div[4]/div[1]/div[2]/div[3]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#level 10
wait = WebDriverWait(driver, 10)
for i in range(1, 6):
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mole.active")))
    driver.execute_script("arguments[0].click();", element)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#level 11
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[244]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[219]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 12
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

#Level 13
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[4]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[5]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[9]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[12]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[13]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[14]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[15]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[16]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 14
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[34]/div').click()
time.sleep(2)

#Level 15


#Level 16
svg_element = driver.find_element(By.CSS_SELECTOR, "svg")
    
    # 2. Get exact dimensions
rect = driver.execute_script("""
        let rect = document.querySelector('svg').getBoundingClientRect();
        return {w: rect.width, h: rect.height, top: rect.top};
    """)
radius = rect['w'] * 0.2  # Increased radius; 0.1 is very tiny
vertical_lift = rect['h'] * 0.05 # Lifts the center by 5% of the total height
steps = 25 # Smooth high-definition circle
actions.move_to_element_with_offset(svg_element, radius, -vertical_lift)
actions.click_and_hold().perform()
for i in range(1, steps + 1):
    theta = (2 * math.pi * i) / steps
    prev_theta = (2 * math.pi * (i - 1)) / steps
            # Calculate the movement delta (change)
    dx = radius * (math.cos(theta) - math.cos(prev_theta))
    dy = radius * (math.sin(theta) - math.sin(prev_theta))
        
    actions.move_by_offset(dx, dy)
    if i % 2 == 0:
        actions.perform()
        actions = ActionChains(driver)
        time.sleep(0.001) 

actions.release().perform()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 17
while True:
        try:
            # Wait for at least one element to be present
            # We use a partial selector for the 'src' attribute
            wait = WebDriverWait(driver, 5)
            hydrants = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//img[contains(@src, 'hydrants')]")
            ))

            if not hydrants:
                break

            # Click the first available hydrant
            hydrants[0].click()
            
            # Brief pause to allow the DOM to update
            time.sleep(0.5)

        except:
            # If no more elements are found or the page changes, we exit
            print("No more hydrants found or page updated.")
            break
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 18
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys(driver.find_element(By.CLASS_NAME, "letters").text.strip().replace("\n","")+"\n")
time.sleep(1)

#Level 19
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys("Butterfly")
driver.find_element(By.CLASS_NAME, "captcha-button-valid").click()
time.sleep(1)

#Level 20
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[5]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[3]/div').click()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[4]')).perform()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[7]')).perform()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[3]/div').click()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[5]')).perform()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[8]')).perform()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[2]/div[2]').click()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]')).perform()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]')).perform()
actions.context_click(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[3]')).perform()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[3]/div').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(3)

#Level 21
for i in range(9):
    driver.find_element(By.CSS_SELECTOR, ".duck.roaming").click()
driver.find_element(By.ID, "captcha-verify-button").click()

#Level 22

#Level 23
text=""
for i in range(1,7):
    text+=driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div[5]/span[{i}]').get_attribute("innerHTML").strip()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/input').send_keys(text)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/input').send_keys("8")
driver.find_element(By.ID, "captcha-verify-button").click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/input').send_keys("34")
driver.find_element(By.ID, "captcha-verify-button").click()

squares = driver.find_elements(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div/div')
colors = [s.value_of_css_property("background-color") for s in squares]
for i, color in enumerate(colors):
    if colors.count(color) == 1:
        print(f"Clicking square {i+1} with unique color: {color}")
        squares[i].click()
        break
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
#Level 24

#Level 25

#Level 26
def square(i):
    return f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]'
#Red
actions.click_and_hold(driver.find_element(By.XPATH, square(1))) \
    .move_to_element(driver.find_element(By.XPATH, square(7))) \
    .move_to_element(driver.find_element(By.XPATH, square(13))) \
    .move_to_element(driver.find_element(By.XPATH, square(19))) \
    .move_to_element(driver.find_element(By.XPATH, square(25))) \
    .move_to_element(driver.find_element(By.XPATH, square(31))) \
    .move_to_element(driver.find_element(By.XPATH, square(32))) \
    .move_to_element(driver.find_element(By.XPATH, square(26))) \
    .move_to_element(driver.find_element(By.XPATH, square(20))) \
    .move_to_element(driver.find_element(By.XPATH, square(21))) \
    .move_to_element(driver.find_element(By.XPATH, square(22))) \
    .release(driver.find_element(By.XPATH, square(28))) \
    .perform()
#Yellow
actions.click_and_hold(driver.find_element(By.XPATH, square(4))) \
    .move_to_element(driver.find_element(By.XPATH, square(3))) \
    .move_to_element(driver.find_element(By.XPATH, square(2))) \
    .move_to_element(driver.find_element(By.XPATH, square(8))) \
    .release(driver.find_element(By.XPATH, square(14))) \
    .perform()
#Pink
actions.click_and_hold(driver.find_element(By.XPATH, square(9))) \
    .release(driver.find_element(By.XPATH, square(15))) \
    .perform()
#orange
actions.click_and_hold(driver.find_element(By.XPATH, square(27))) \
    .move_to_element(driver.find_element(By.XPATH, square(33))) \
    .move_to_element(driver.find_element(By.XPATH, square(34))) \
    .move_to_element(driver.find_element(By.XPATH, square(35))) \
    .release(driver.find_element(By.XPATH, square(29))) \
    .perform()
#Blue
actions.click_and_hold(driver.find_element(By.XPATH, square(6))) \
    .move_to_element(driver.find_element(By.XPATH, square(5))) \
    .move_to_element(driver.find_element(By.XPATH, square(11))) \
    .move_to_element(driver.find_element(By.XPATH, square(10))) \
    .release(driver.find_element(By.XPATH, square(16))) \
    .perform()
#purple
actions.click_and_hold(driver.find_element(By.XPATH, square(12))) \
    .move_to_element(driver.find_element(By.XPATH, square(18))) \
    .move_to_element(driver.find_element(By.XPATH, square(17))) \
    .move_to_element(driver.find_element(By.XPATH, square(23))) \
    .move_to_element(driver.find_element(By.XPATH, square(24))) \
    .move_to_element(driver.find_element(By.XPATH, square(30))) \
    .release(driver.find_element(By.XPATH, square(36))) \
    .perform()
driver.find_element(By.ID, 'captcha-verify-button').click()
time.sleep(1)

#Level 27

#Level 28
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[6]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]').click()
driver.find_element(By.ID, 'captcha-verify-button').click()
time.sleep(1)

#Level 29

#Level 30
for i in range(2,17):
    if i!=4:
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, 'captcha-verify-button').click()
time.sleep(1)

#Level 31
def solve_memory_level(driver):
    # 1. Identify all tiles
    tiles = driver.find_elements(By.CSS_SELECTOR, ".launchpad-pad")
    
    # Store the 'idle' class string (e.g., "dance-square launchpad-pad")
    default_class = "dance-square launchpad-pad"
    
    sequence = []
    print("Watching for flashes... (Wait for the game to finish showing the pattern)")
    
    # 2. Observation Phase
    # We loop until we see no changes for 2 seconds (indicating the pattern is over)
    last_flash_time = time.time()
    last_tile_index = -1
    
    while time.time() - last_flash_time < 2.0:
        for i, tile in enumerate(tiles):
            current_class = tile.get_attribute("class")
            
            # Check if the class is DIFFERENT from the idle state
            if current_class != default_class:
                # To prevent recording the same flash multiple times:
                if i != last_tile_index:
                    sequence.append(tiles[i])
                    last_tile_index = i
                    last_flash_time = time.time()
                    print(f"Recorded flash at tile {i}")
                    
        # Small delay to prevent CPU maxing out
        time.sleep(0.05)
        
        # Timeout if we've been watching for 20 seconds with no flashes at all
        if len(sequence) == 0 and time.time() - last_flash_time > 10:
            print("No flashes detected. Check if the class names are correct.")
            return

    # 3. Playback Phase
    print(f"Pattern ended. Clicking {len(sequence)} tiles...")
    time.sleep(0.5) # Short pause before responding
    
    for tile in sequence:
        try:
            tile.click()
        except Exception as e:
            print(f"Click failed: {e}")
for _ in range(3):
    solve_memory_level(driver)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 32
results = []
for i in range(1, 6):
            filename =  driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div[2]/img[{i}]').get_attribute("src").split("/not-a-robot/brands/")[1]
            first_letter = filename[0]
            results.append(first_letter)
final_word = "".join(results)
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys(final_word)
driver.find_element(By.CLASS_NAME, "captcha-button-valid").click()
time.sleep(1)

#Level 33
parsed_data = []

for item in driver.find_elements(By.CSS_SELECTOR, ".math-grid-item"):
    value_text = item.find_element(By.CLASS_NAME, "math-grid-term-actual").get_attribute("textContent").strip()
    if not value_text:
        continue # Skip if truly empty         
    if "Infinity" in value_text:
            value = float('inf')
    else:
        cleaned_value = "".join(c for c in value_text if c.isdigit() or c == '.')
        value = float(cleaned_value)
    parsed_data.append({
        'element': item,
        'value': value
    })
parsed_data.sort(key=lambda x: x['value'])
for entry in parsed_data:
    entry['element'].click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 34
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="34":
    driver.find_element(By.CLASS_NAME, "ball").click()
    driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 35

#Level 36
srcs=["https://neal.fun/not-a-robot/imposters/9.webp",
"https://neal.fun/not-a-robot/imposters/6.webp",
"https://neal.fun/not-a-robot/imposters/1.webp"]
for i in range(1,10):
    if driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]/img').get_attribute("src") in srcs:
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 37

#Level 38

#Level 39

#Level 40

#Level 41

#Level 42

#Level 43

#Level 44
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="44":
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Chat with Jessica..."]').send_keys("were done\n")
    time.sleep(1)
    driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 45
for i in range(409,419):
    driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 46

#Level 47
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div/div[2]/div/img').click()
driver.execute_script("document.querySelector('video').currentTime = 87;")
time.sleep(2)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
keyboard.wait(' ')
driver.quit()