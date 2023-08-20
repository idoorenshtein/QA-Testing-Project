from selenium.webdriver.common.by import By

pim_configuration = (By.CSS_SELECTOR, 'i[class="oxd-icon bi-chevron-down"]')
employee_list = (By.CSS_SELECTOR, 'li[class="oxd-topbar-body-nav-tab --visited"]')
add_employee = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
reports = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a')


class UpperPim:
    def __init__(self, driver):
        self.driver = driver

    def get_pim_configuration(self):
        return self.driver.find_element(pim_configuration[0], pim_configuration[1])

    def get_employee_list(self):
        return self.driver.find_element(employee_list[0], employee_list[1])

    def get_add_employee(self):
        return self.driver.find_element(add_employee[0], add_employee[1])

    def get_reports(self):
        return self.driver.find_element(reports[0], reports[1])

