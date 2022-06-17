from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#gets credentials from userInfo.py if it exists, else get credentials from user input
try:
    import userInfo
    credentials = userInfo.credentials
except ModuleNotFoundError:
    credentials = dict()
    credentials["username"] = input('Username: ')
    credentials["password"] = input('Password: ')


if __name__ == "__main__":
    activity = input('Activity (jwc rock wall, badminton): ')

    #initiates chrome driver and goes to ucla rec website
    URL = "https://secure.recreation.ucla.edu/Program/GetProducts"
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(URL)

    #chooses sso to login
    login = driver.find_element(By.ID, "loginLink")
    login.click()
    sso = driver.find_element(By.XPATH, "//div[@id='section-sign-in-first']//button[@title='CLICK HERE FOR UCLA LOGON']")
    
    time.sleep(1)
   
    sso.click()
   
    time.sleep(1)
    
    #logs in with credentials
    driver.find_element(By.ID, "logon").send_keys(credentials["username"])
    driver.find_element(By.ID, "pass").send_keys(credentials["password"])

    driver.find_element(By.NAME, "_eventId_proceed").click()

    #searches for activity
    search = driver.find_element(By.ID, 'txtSearch')
    search.send_keys(activity)
    search.send_keys(Keys.ENTER)

    time.sleep(1)

    #clicks on activity
    driver.find_element(By.ID, 'list-group').click()

    time.sleep(1000)
    driver.quit()