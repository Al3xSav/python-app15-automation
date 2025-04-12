import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpage
        self.driver.get("https://demoqa.com/login")

        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        login_button = self.driver.find_element(By.ID, "login")

        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Elements dropdown
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]')))
        elements.click()

        text_box = password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "item-0")))
        text_box.click()

        # Locate the form Fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))
        email_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "userEmail")))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "currentAddress")))
        perma_address_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "permanentAddress")))
        submit_button = self.driver.find_element(By.ID, "submit")

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        perma_address_field.send_keys(permanent_address)

        # Submit the form
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate the Upload and Download section and the Download Button
        upload_download = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "item-7")))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        try:
            if self.driver:
                self.driver.close()  # Better than .close(), it ends the whole session safely
                self.driver = None
        except Exception as e:
            print(f"[ERROR] Could not close browser: {e}")

if __name__ == "__main__":
    WebAutomation = WebAutomation()
    WebAutomation.login("al3xsav", "Sa8565!!")
    WebAutomation.fill_form("John Smothing", "5Hx2A@example.com", "Current Address", "Permanent Address")
    WebAutomation.download()
    WebAutomation.close()