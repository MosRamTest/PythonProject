import time
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

from Tests.conftest import setup
from utils.readProperties_data import ReadConfig_data


def loginToNdosi(driver, username, password):
    hp = HomePage(driver)
    hp.verifyNdosiHeading()
    hp.clickLearningMaterial()
    time.sleep(2)
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_loginBtn()