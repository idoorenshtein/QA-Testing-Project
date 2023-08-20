import allure
from selenium.common.exceptions import TimeoutException
import page_objects.web_objects.main_page as main
import page_objects.web_objects.add_employee_page
import page_objects.web_objects.pim_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:
    @staticmethod
    @allure.step('login to OrangeHrm flow')
    def login_flow(user: str, password: str):
        UiActions.Update_text(page.web_login.get_user_name(), user)
        UiActions.Update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())

    @staticmethod
    @allure.step('verify OrangeHrm title flow')
    def verify_OrangeHrm_title(expected: str):
        wait(For.ELEMENT_EXISTS, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('verify displayed menu button flow sing smart-assertions')
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_user_dropdown(),
                 page.web_upper_menu.get_help_button()]
        Verifications.soft_assert(elems)

    @staticmethod
    @allure.step('go to pim flow')
    def open_pim():
        UiActions.click(page.web_left_menu.get_PIM())

    @staticmethod
    @allure.step('create new employee flow')
    def create_employee(first_name, last_name):
        UiActions.click(page.web_upper_pim.get_add_employee())
        UiActions.Update_text(page.web_add_employee.get_first_name(), first_name)
        UiActions.Update_text(page.web_add_employee.get_last_name(), last_name)
        UiActions.click(page.web_add_employee.get_save())
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.pim_page.loader_element)

    @staticmethod
    @allure.step('search employee from employee table flow')
    def verify_employee_csv(search_value, expected):
        UiActions.click(page.web_upper_pim.get_employee_list())
        UiActions.Update_text(page.web_pim.get_employee_name(), search_value)
        UiActions.click(page.web_pim.get_search_employee())
        try:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.pim_page.loader_element)
            Verifications.verify_number_of_elements(page.web_pim.get_employee_cards(), int(expected))
        except TimeoutException:
            Verifications.verify_number_of_elements(page.web_pim.get_employee_cards(), int(expected))

    @staticmethod
    @allure.step('delete employee from employee table flow')
    def delete_employee_card(fullname):
        UiActions.click(page.web_upper_pim.get_employee_list())
        UiActions.Update_text(page.web_pim.get_employee_name(), fullname)
        UiActions.click(page.web_pim.get_search_employee())
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.pim_page.loader_spinner)
        UiActions.click(page.web_pim.get_delete_employee())
        UiActions.click(page.web_pim.get_confirm_delete())
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.pim_page.loader_element)

    @staticmethod
    @allure.step('go to home flow')
    def home(self):
        self.driver.get(get_data('Url'))


data = read_csv(get_data('CSV_Location'))
testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]

