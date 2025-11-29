import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ndosiautomation.co.za/")

driver.find_element(By.ID, "overview-hero").is_displayed()


Welcome_text = driver.find_element(By.XPATH, '//*[@id="overview-hero"]/h2').text

if Welcome_text == "Learn Automation the Right Way":
    print("Test Passed: Welcome text is correct.")
    assert True
else:
    print("Test Failed: Welcome text is incorrect.")
    assert False

driver.find_element(By.ID, "nav-btn-practice").click()
driver.find_element(By.ID, "login-email").send_keys("king@gmail.com")
driver.find_element(By.ID, "login-password").send_keys("King1234")
driver.find_element(By.ID, "login-submit").click()
time.sleep(2)
driver.find_element(By.ID, "practice-heading").is_displayed()
time.sleep(5)


