import math
import time
import keyboard
from collections import deque
# Selenium Core
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# Selenium Wait & Exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from asyncio import wait

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
behemoth_script = """
        try {
            var val = window.document.doctype.nextSibling.children[0].nextElementSibling.children[0].__vue__._scope.effects[3].deps[0].subs[1].vm._scope.effects[0].deps[1].subs[0].vm.$options.parent.$options._parentVnode.elm.children[0].children[0].__vue__._scope.effects[0].deps[0].subs[1].deps[6].subs[0].vm.$options._parentVnode.elm.previousElementSibling.children[0].nextElementSibling.nextElementSibling.children[0].__vue__._scope.effects[0].deps[0].subs[1].deps[1].subs[1].vm.captchaText;
            return val;
        } catch (e) {
            return "Error: Path not ready or changed. " + e.message;
        }
        """
captcha_text = driver.execute_script(behemoth_script)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[3]/div/input').send_keys(captcha_text)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[3]/button').click()
time.sleep(1)
#Level 17
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

#Level 18
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

#Level 19
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys(driver.find_element(By.CLASS_NAME, "letters").text.strip().replace("\n","")+"\n")
time.sleep(1)

#Level 20
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys("Butterfly")
driver.find_element(By.CLASS_NAME, "captcha-button-valid").click()
time.sleep(1)

#Level 21
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

#Level 22
for i in range(9):
    driver.find_element(By.CSS_SELECTOR, ".duck.roaming").click()
driver.find_element(By.ID, "captcha-verify-button").click()

#Level 23
canvas = driver.find_element(By.XPATH, '//*[@id="panorama"]/div[1]/div[1]')

actions.click_and_hold(canvas) \
       .move_by_offset(700, 0) \
       .release() \
       .perform()
actions.click_and_hold(canvas) \
       .move_by_offset(700, -100) \
       .release() \
       .perform()
zoom=driver.find_element(By.XPATH, '//*[@id="panorama"]/div[1]/div[6]/div[1]/div[1]')

for i in range(12):
    zoom.click()
    time.sleep(0.1)
driver.find_element(By.ID,"captcha-verify-button").click()
time.sleep(1)

#Level 24
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
#Level 25
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]').click()
driver.find_element(By.ID, "express-canvas").click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div[2]').click()
driver.find_element(By.ID, "express-canvas").click()
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div[3]').click()
driver.find_element(By.ID, "express-canvas").click()
driver.execute_script("document.querySelector('.color-picker-hidden').value ='#FF0000';document.querySelector('.color-picker-hidden').dispatchEvent(new Event('input', { bubbles: true }));")
for i in range(8):
    driver.find_element(By.ID, "express-canvas").click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
#Level 26

#Level 27
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

#Level 28

#Level 29
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[6]').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]').click()
driver.find_element(By.ID, 'captcha-verify-button').click()
time.sleep(1)

#Level 30

TILE_MAP = {
    "0% 0%": 0, "50% 0%": 1, "100% 0%": 2,
    "0% 50%": 3, "50% 50%": 4, "100% 50%": 5,
    "0% 100%": 6, "50% 100%": 7, "None": 8  # 8 is the empty slot
}

def solve_puzzle_bfs(start_state):
    goal = tuple(range(9))
    # Queue stores (current_state, path_of_tile_values_moved)
    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path

        empty_idx = current.index(8)
        r, c = divmod(empty_idx, 3)

        # Potential moves: Right, Left, Down, Up
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < 3 and 0 <= nc < 3:
                neighbor_idx = nr * 3 + nc
                new_state = list(current)
                # Swap empty spot with the neighbor tile
                new_state[empty_idx], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[empty_idx]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    # We record the value of the tile we just moved into the empty space
                    queue.append((new_state, path + [current[neighbor_idx]]))

def scrape_board(driver):
    tiles = driver.find_elements(By.CSS_SELECTOR, ".puzzle-tile")
    board = [None] * 9
    
    for tile in tiles:
        # Calculate grid position based on style="top: X%; left: Y%;"
        left_str = tile.get_attribute("style").split("left: ")[1].split("%")[0]
        top_str = tile.get_attribute("style").split("top: ")[1].split("%")[0]
        
        col = int(float(left_str) // 33)
        row = int(float(top_str) // 33)
        grid_pos = row * 3 + col
        
        if "empty-tile" in tile.get_attribute("class"):
            board[grid_pos] = 8
        else:
            img = tile.find_element(By.CLASS_NAME, "tile-image")
            bg_pos = img.value_of_css_property('background-position')
            board[grid_pos] = TILE_MAP.get(bg_pos)
            
    return tuple(board)

initial_state = scrape_board(driver)
moves = solve_puzzle_bfs(initial_state)

# 3. Execute clicks
for tile_value in moves:
    all_tiles = driver.find_elements(By.CSS_SELECTOR, ".puzzle-tile:not(.empty-tile)")
    for t in all_tiles:
        img = t.find_element(By.CLASS_NAME, "tile-image")
        if TILE_MAP.get(img.value_of_css_property('background-position')) == tile_value:
            t.click()
            time.sleep(0.4) # Brief pause for the slide animation to finish
            break
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 31
for i in range(2,17):
    if i!=4:
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, 'captcha-verify-button').click()
time.sleep(1)

#Level 32
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

#Level 33
results = []
for i in range(1, 6):
            filename =  driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div[2]/img[{i}]').get_attribute("src").split("/not-a-robot/brands/")[1]
            first_letter = filename[0]
            results.append(first_letter)
final_word = "".join(results)
driver.find_element(By.CLASS_NAME, "captcha-input-text").send_keys(final_word)
driver.find_element(By.CLASS_NAME, "captcha-button-valid").click()
time.sleep(1)

#Level 34
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

#Level 35
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="34":
    driver.find_element(By.CLASS_NAME, "ball").click()
    driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 36
def get_score():
    try:
        score_element = driver.find_element(By.CSS_SELECTOR, ".stat-value")
        return int(score_element.text.replace(',', ''))
    except:
        return 0

def is_match(g, idx):
    if not g[idx]: return False
    r, c = divmod(idx, 8)
    color = g[idx]
    
    # Horizontal Check
    h_count = 1
    for i in range(c - 1, -1, -1):
        if g[r * 8 + i] == color: h_count += 1
        else: break
    for i in range(c + 1, 8):
        if g[r * 8 + i] == color: h_count += 1
        else: break
    if h_count >= 3: return True

    # Vertical Check
    v_count = 1
    for i in range(r - 1, -1, -1):
        if g[i * 8 + c] == color: v_count += 1
        else: break
    for i in range(r + 1, 8):
        if g[i * 8 + c] == color: v_count += 1
        else: break
    return v_count >= 3

def find_any_match():
    """Scans for the first available move in either direction."""
    cells = driver.find_elements(By.CLASS_NAME, "candy-cell")
    grid = []
    for cell in cells:
        try:
            grid.append(cell.find_element(By.TAG_NAME, "svg").get_attribute("class"))
        except:
            grid.append(None)

    for i in range(len(grid)):
        r, c = divmod(i, 8)
        
        # 1. Try Horizontal (Right)
        if c < 7:
            temp = list(grid)
            temp[i], temp[i+1] = temp[i+1], temp[i]
            if is_match(temp, i) or is_match(temp, i+1):
                return cells[i], Keys.ARROW_RIGHT

        # 2. Try Vertical (Down)
        if r < 7:
            temp = list(grid)
            temp[i], temp[i+8] = temp[i+8], temp[i]
            if is_match(temp, i) or is_match(temp, i+8):
                return cells[i], Keys.ARROW_DOWN
                
    return None, None

# --- Main Loop ---
while True:
    if get_score() >= 1000:
        print("Success! 1000 points reached.")
        break

    element, key_to_press = find_any_match()

    if element:
        try:
            element.click()
            time.sleep(0.05)
            element.send_keys(key_to_press)
            time.sleep(1.4) # Wait for drop animation
        except:
            continue
    else:
        # No matches found, force a board shuffle
        print("No matches. Shuffling...")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
        time.sleep(1.0)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
#Level 37
srcs=["https://neal.fun/not-a-robot/imposters/9.webp",
"https://neal.fun/not-a-robot/imposters/6.webp",
"https://neal.fun/not-a-robot/imposters/1.webp"]
for i in range(1,10):
    if driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]/img').get_attribute("src") in srcs:
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 38

#Level 39

#Level 40
def get_live_y(reel_id):
    return driver.execute_script("""
        var el = document.getElementById(arguments[0]);
        var style = window.getComputedStyle(el);
        var trans = style.translate || style.transform;
        if (!trans || trans === 'none') return 0;
        var y = trans.split(' ').pop();
        return Math.abs(parseFloat(y));
    """, reel_id)

def solve_with_timing():
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "captcha-input-text")))
    
    # 1. PRE-SCAN: Get all target characters first
    targets = []
    for i in range(5):
        reel_id = f"slot-reel-{i}"
        reel_element = driver.find_element(By.ID, reel_id)
        
        # Wait until the span inside the reel actually has text
        char = ""
        while not char:
            slots = reel_element.find_elements(By.CLASS_NAME, "slot-letter")[:5]
            for idx, slot in enumerate(slots):
                spans = slot.find_elements(By.TAG_NAME, "span")
                if spans and spans[0].text.strip():
                    char = spans[0].text.strip()
                    targets.append({"char": char, "idx": idx, "id": reel_id})
                    break
            if not char: time.sleep(0.1) # Brief wait if DOM isn't ready

    # 2. SNIPE: Execute the rhythm-based typing
    for target in targets:
        target_y = target["idx"] * 10
        char = target["char"]
        reel_id = target["id"]
        
        print(f"Targeting Reel {reel_id[-1]}: Sniping '{char}' at {target_y}%")

        while True:
            current_y = get_live_y(reel_id)
            
            # Adjust the 1.5 margin if the script skips the target or fires late
            if abs(current_y - target_y) < 1.5:
                input_field.send_keys(char)
                print(f"SUCCESS: Fired {char}")
                time.sleep(0.5) # Wait for the reel-stop animation to trigger
                break

    # 3. SUBMIT
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "captcha-button").click()

solve_with_timing()
time.sleep(1)

#Level 41

#Level 42

#Level 43

#Level 44

#Level 45
while driver.execute_script("return window.localStorage.getItem('not-a-robot-level');")=="44":
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Chat with Jessica..."]').send_keys("were done\n")
    time.sleep(1)
    driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 46
for i in range(409,419):
    driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 47

#Level 48
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div/div[2]/div/img').click()
driver.execute_script("document.querySelector('video').currentTime = 87;")
time.sleep(2)
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)
keyboard.wait(' ')
driver.quit()