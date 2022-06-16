from modulefinder import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import argparse
from getpass import getpass

try:
    import userInfo
except ModuleNotFoundError:
    pass

parser = argparse.ArgumentParser(description="Logging into UCLA networks")
parser.add_argument("username")
args = parser.parse_args()
args.password = getpass("Please enter your UCLA password: ")

if ('userInfo' not in locals()):
    credentials = args.__dict__
else:
    credentials = userInfo.credentials

if __name__ == "__main__":
    URL = "https://secure.recreation.ucla.edu/Program/GetProducts"
    driver = webdriver.Chrome()
    driver.get(URL)

    login = driver.find_element(By.ID, "loginLink")
    login.click()
    driver.implicitly_wait(1)
    sso = driver.find_element(By.XPATH, "//div[@id='section-sign-in-first']//button[@title='CLICK HERE FOR UCLA LOGON']")
    driver.implicitly_wait(5)
   
    time.sleep(2)
   
    sso.click()
   
    time.sleep(1)
    
    driver.find_element(By.ID, "logon").send_keys(credentials["username"])
    driver.find_element(By.ID, "pass").send_keys(credentials["password"])

    driver.find_element(By.NAME, "_eventId_proceed").click()

    time.sleep(1)

    all_classifications = driver.find_element(By.ID, "00000000-0000-0000-0000-000000000000")
    all_classifications.click()
    time.sleep(20)
    driver.quit()