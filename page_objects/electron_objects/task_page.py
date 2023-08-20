from selenium.webdriver.common.by import By

create = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.CLASS_NAME, 'view_2Ow90')
delete_button = (By.XPATH, "//div[@class='view_2Ow90']/*[name()='svg']")


class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(create[0], create[1])

    def get_tasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_button[0], delete_button[1])
