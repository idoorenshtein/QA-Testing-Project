from selenium.webdriver.common.by import By

user_name = (By.NAME, 'username')
password = (By.NAME, 'password')
submit = (By.XPATH, "//button[@type='submit']")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_submit(self):
        return self.driver.find_element(submit[0], submit[1])