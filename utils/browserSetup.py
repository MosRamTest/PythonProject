from utils.readProperties_data import ReadConfig_data
from selenium import webdriver

def setup_Browser(driver):
    dev_url = ReadConfig_data().getURL()
    driver.get(dev_url)
    driver.maximize_window()
    return driver
