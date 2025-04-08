from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/login")

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
login_button = driver.find_element(By.ID, "login")

username_field.send_keys("al3xsav")
password_field.send_keys("Sa8565!!")
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown
elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]')))
elements.click()

text_box = password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item-0")))
text_box.click()

# Locate the form Fields and submit button
fullname_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userEmail")))
current_address_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "currentAddress")))
perma_address_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "permanentAddress")))
submit_button = driver.find_element(By.ID, "submit")

# Fill in the form fields
fullname_field.send_keys("John Doe")
email_field.send_keys("jdoe@ex.com")
current_address_field.send_keys("123 Main St")
perma_address_field.send_keys("456 Main St")

# Submit the form
driver.execute_script("arguments[0].click();", submit_button)

input("Press enter to close")
driver.close()