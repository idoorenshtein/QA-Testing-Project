from selenium.webdriver.common.by import By

first_name = (By.NAME, 'firstName')
last_name = (By.NAME, 'lastName')
save = (By.CSS_SELECTOR, 'button[type="submit"]')
employee_details = (By.CLASS_NAME, 'orangehrm-edit-employee-navigation')


class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_name(self):
        return self.driver.find_element(first_name[0], first_name[1])

    def get_last_name(self):
        return self.driver.find_element(last_name[0], last_name[1])

    def get_save(self):
        return self.driver.find_element(save[0], save[1])

    def get_employee_details(self):
        return self.driver.find_element(employee_details[0], employee_details[1])