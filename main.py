from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# gets credentials from userInfo.py if it exists, else get credentials from user input
try:
    import userInfo
    credentials = userInfo.credentials
    desired_events = userInfo.desired_events
except ModuleNotFoundError:
    credentials = dict()
    credentials["username"] = input('Username: ')
    credentials["password"] = input('Password: ')
    credentials["activity"] = input('Activity (jwc rock wall, badminton): ')
    desired_time = input('Time Range: Start_Time(AM/PM) - End_Time(AM/PM): ')
    desired_day = input('Day: ')



if __name__ == "__main__":
    # initiates chrome driver and goes to ucla rec website
    URL = "https://secure.recreation.ucla.edu/Program/GetProducts"
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(URL)

    # chooses sso to login
    login = driver.find_element(By.ID, "loginLink")
    login.click()

    time.sleep(2)

    sso = driver.find_element(By.XPATH, "//div[@id='section-sign-in-first']//button[@title='CLICK HERE FOR UCLA LOGON']")
    
    time.sleep(2)
   
    sso.click()
   
    time.sleep(2)
    
    # logs in with credentials
    driver.find_element(By.ID, "logon").send_keys(credentials["username"])
    driver.find_element(By.ID, "pass").send_keys(credentials["password"])

    driver.find_element(By.NAME, "_eventId_proceed").click()
    driver.switch_to.window(driver.current_window_handle)

    # searches for activity
    search = driver.find_element(By.ID, 'txtSearch')
    search.send_keys(credentials["activity"])
    search.send_keys(Keys.ENTER)

    time.sleep(1)

    # clicks on activity
    driver.find_element(By.ID, 'list-group').click()

    time.sleep(1)

    # gathers all events and parses their dates
    events = driver.find_elements(By.XPATH,"//div[@id='main']//section[@class='list-group']//div[@class]//div[@data-instance-id]")
    if ("userInfo" in globals()):
        for event in events:
            date = event.get_attribute("data-instance-dates")
            day = date.split(',')[0]
            time_range = event.get_attribute("data-instance-times")
            if ([day, time_range] in userInfo.desired_events):
                path = "//div[@id='main']//section[@class='list-group']//div[@class]//div[@data-instance-dates='{date}' and @data-instance-times='{time_range}']//button".format(**locals())
                print(path)
                driver.find_element(By.XPATH, path).click()
                break
    else:
        for event in events:
            day = event.get_attribute("data-instance-dates")[0]
            time_range = event.get_attribute("data-instance-times")
            if (day == desired_day and time_range == desired_time):
                path = "//div[@id='main']//section[@class='list-group']//div[@class]//div[@data-instance-dates='{date}' and @data-instance-times='{time_range}']//button".format(**locals())
                driver.find_element(By.XPATH, path).click()
                break
    
    time.sleep(1)

    # finds button to find waiver and accepts
    driver.find_element(By.ID, "btnAccept").click()

    time.sleep(1)

    driver.find_element(By.ID, "checkoutButton").click() 

    time.sleep(1)

    driver.find_element(By.XPATH, "//div[@id='CheckoutModal']//button[@onclick='Submit()']").click()

    driver.quit()