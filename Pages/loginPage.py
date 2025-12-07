from selenium.webdriver.common.by import By


class LoginPage:
    txt_loginEmail_id = "login-email"
    txt_password_id = "login-password"
    btn_loginBtn_id = "login-submit"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,  username):
        username_field = self.driver.find_element(By.ID, self.txt_loginEmail_id)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, self.txt_password_id)
        password_field.clear()
        password_field.send_keys(password)

    def click_loginBtn(self):
        login_button = self.driver.find_element(By.ID, self.btn_loginBtn_id)
        login_button.click()
