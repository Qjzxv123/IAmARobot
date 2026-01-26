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



# Initialize the Chrome Driver
driver = webdriver.Chrome()


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
    driver.find_element(By.XPATH, "//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div/div[3]/div/input").send_keys("FNZZSD")
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
for i in range(1, 9):
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
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[6]/img').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[7]/img').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[8]/img').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[9]/img').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[11]/img').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[15]/img').click()
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 13
srcs = [
"https://neal.fun/not-a-robot/muffins/chihuahuas/1.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/4.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/2.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/5.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/6.webp",
"https://neal.fun/not-a-robot/muffins/chihuahuas/3.webp"
]
for i in range(1, 16):
    if driver.find_element(By.XPATH,f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]/img').get_attribute("src") in srcs:
        driver.find_element(By.XPATH,f'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[2]/div/div/div[{i}]').click() 
driver.find_element(By.ID, "captcha-verify-button").click()
time.sleep(1)

#Level 14
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

#Level 15
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div/div[34]/div').click()
time.sleep(1)

#Level 16
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
time.sleep(1)

#Level 17
