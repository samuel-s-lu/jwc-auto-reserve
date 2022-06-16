from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
time.sleep(5)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert 'No results found.' not in driver.page_source
driver.quit()
