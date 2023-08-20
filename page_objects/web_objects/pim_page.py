from selenium.webdriver.common.by import By

employee_name = (By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]')
search_employee = (By.CSS_SELECTOR, 'button[type="submit"]')
employee_cards = (By.CLASS_NAME, 'oxd-table-card')
delete_employee = (By.XPATH, '//div[9]/div/button[1]')
confirm_delete = (By.CSS_SELECTOR, 'i[class="oxd-icon bi-trash oxd-button-icon"]')
loader_element = (By.XPATH, "//div[@id='oxd-toaster_1']/div")
loader_spinner = (By.CLASS_NAME, 'oxd-loading-spinner')


class PimPage:
    def __init__(self, driver):
        self.driver = driver

    def get_employee_name(self):
        return self.driver.find_element(employee_name[0], employee_name[1])

    def get_search_employee(self):
        return self.driver.find_element(search_employee[0], search_employee[1])

    def get_employee_cards(self):
        return self.driver.find_elements(employee_cards[0], employee_cards[1])

    def get_delete_employee(self):
        return self.driver.find_element(delete_employee[0], delete_employee[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])

    def get_loader_element(self):
        return self.driver.find_element(loader_element[0], loader_element[1])

    def get_employee_by_index(self):
        index = 1
        return self.get_employee_cards()[index]
