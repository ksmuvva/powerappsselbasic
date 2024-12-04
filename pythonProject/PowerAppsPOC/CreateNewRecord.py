import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

custody_name = "Kate Sunders"
date_of_birth = "12/10/1972"
custody_officer_name = "Phillips Anderson"

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Edge(options=options)

driver.get("https://make.powerapps.com/environments/14298897-3749-e6dd-a921-2d22676009a0/home")
driver.maximize_window()
time.sleep(15)

actual_title = driver.title
expected_title = 'Power Apps | Home'

if actual_title == expected_title:
    print("CustodyRecord Login Successful")
else:
    print("CustodyRecord Login Failed")
time.sleep(5)
driver.find_element(By.ID, "ms-searchux-input-0").send_keys("DCCM")
driver.find_element(By.CSS_SELECTOR, '[title=Search]').click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '[role=link]').click()
time.sleep(2)

handles = driver.window_handles
driver.switch_to.window(handles[1])

time.sleep(3)
driver.find_element(By.ID, "i0118").send_keys("Update321")
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(1)
driver.find_element(By.ID, "idSIButton9").click()

time.sleep(20)

driver.find_element(By.CSS_SELECTOR, '[alt=New]').click()

wait = WebDriverWait(driver, 30)

detainee_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Detainee Name']")))
detainee_name.send_keys(custody_name)

time.sleep(2)
dob_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Date of Date Of Birth']")))
dob_field.send_keys(date_of_birth)

wait = WebDriverWait(driver, 15)

dropdown_field = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='fui-Dropdown ___zlnjpn0 f1aa9q02 f16jpd5f "
                   "f1jar5jt fyu767a f1ewtqcl ftuwxu6 fy77jfu f10pi13n f14a1fxs "
                   "f3e99gv fhljsf7 f1gw3sf2 f13zj6fq f1mdlcz9 f1a7op3 f1gboi2j "
                   "f1cjjd47 ffyw7fx f1kp91vd f1ibwz09 f14pi962 f1lh990p f1jc6hxc "
                   "f13evtba f1yk9hq fhwpy7i f14ee0xe f1xhbsuh fv8e3ye ftb5wc6 "
                   "fjw5xc1 f1xdyd5c fatpbeo fb7uyps f1cmft4k f1x58t8o f1ibeo51 "
                   "f132nw8t f1htdosj f16xq7d1 f192inf7 f5tn483 f1vxd6vx f1ojsxk5 "
                   "fzkkow9 fcdblym fg706s2 fjik90z f1p3nwhy f11589ue f1q5o8ev "
                   "f1pdflbu fly5x3f f1l02sjl']"
         )
    )
)
dropdown_field.click()

male_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='option'][text()='Male']")
    )
)
male_option.click()

time.sleep(2)
nationality = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Nationality']")))
nationality.send_keys("Portugal")

time.sleep(2)
location = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Location']")))
location.send_keys("Brazil")

wait = WebDriverWait(driver, 15)

signature_field = wait.until(
    EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='CR3_Signature_Text']")))
signature_field.click()

# Create an instance of ActionChains
actions = ActionChains(driver)

# Move to the center of the signature field to start drawing
actions.move_to_element(signature_field).move_by_offset(5, 5).click_and_hold().perform()

# Draw a simple signature (e.g., a zigzag)
for _ in range(5):
    actions.move_by_offset(5, 5).perform()
    actions.move_by_offset(-5, 5).perform()

# Release the click
actions.release().perform()

confirm_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Confirm']")))
confirm_button.click()

custody_officer = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Custody Officer Name']")))
custody_officer.send_keys(custody_officer_name)

job_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Job Title']")))
job_title.send_keys("Senior Guard")

time.sleep(10)

save_close = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Save & Close')]")))
save_close.click()

time.sleep(10)


driver.quit()
