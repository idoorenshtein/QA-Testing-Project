from selenium.webdriver.common.by import By

user_dropdown = (By.CSS_SELECTOR, "li[class='oxd-userdropdown']")
question_icon = (By.CSS_SELECTOR, "i[class='oxd-icon bi-question-lg']")


class UpperMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_dropdown(self):
        return self.driver.find_element(user_dropdown[0], user_dropdown[1])

    def get_help_button(self):
        return self.driver.find_element(question_icon[0], question_icon[1])
