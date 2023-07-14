from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigating to the Dominos.ca homepage
driver.get("https://www.dominos.ca/en/")
time.sleep(3)
# Click on Carry-out option.
b1 = driver.find_element("xpath","/html/body/div[3]/div[2]/main/section[1]/div/div/a[2]")
b1.click()
time.sleep(5)
# Enter the place of carry-out
search_bar = driver.find_element("id","cityFinder")
search_bar.send_keys("121 University Avenue East, Waterloo, ON")
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
# Scroll down a bit
SCROLL_PAUSE_TIME = 0.005
driver.execute_script("window.scrollTo(0,600);")
time.sleep(SCROLL_PAUSE_TIME)
time.sleep(5)

# Click on the desired location
location = driver.find_element("xpath", "/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div/button")
location.click()
time.sleep(5)

# Scroll down a bit
driver.execute_script("window.scrollTo(0,600);")
time.sleep(SCROLL_PAUSE_TIME)
time.sleep(5)
# Select item category
item = driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div[2]/div[8]/a[4]/div[1]/img")
item.click()
time.sleep(5)
# Select particular item
item_inside = driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/section/div/div[1]/div/a")
item_inside.click()
time.sleep(5)
# Add to cart
add_order = driver.find_element("xpath", "/html/body/div[4]/div/section/div/div/form/div/button[2]")
add_order.click()
time.sleep(5)
# Click on Cart icon in the Nav Bar
cart = driver.find_element("xpath", "/html/body/header/nav[1]/div[1]/div[4]/a")
cart.click()
time.sleep(10)
# Click on Check out button
checkout = driver.find_element("xpath", "/html/body/div[4]/div/div[3]/div[2]/button[2]/span[2]")
checkout.click()
time.sleep(5)
# No thanks to addition of Drinks
nothanks = driver.find_element("xpath", "/html/body/div[25]/section/div/div[2]/div/a")
nothanks.click()
time.sleep(5)
# Closing the webdriver
driver.close()
