import time

import allure
import pytest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadConfig_data
from utils.commonLogin import loginToNdosi
from Tests.conftest import setup
from utils.browserSetup import setup_Browser


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURL()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginWithValidDetails(self, setup):
        self.driver = setup_Browser(setup)
        loginToNdosi(self.driver, self.username, self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Learning Material Home",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.dev
    def test_loginWithInValidDetails(self, setup):
        self.driver = setup_Browser(setup)
        loginToNdosi(self.driver, self.username, self.password + "Invalid")
        time.sleep(2)
        self.driver.quit()
