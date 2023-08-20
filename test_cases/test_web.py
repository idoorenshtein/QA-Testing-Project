import allure
import pytest
from utilities.common_ops import get_data
from workflows import web_flows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class Test_web:
    @allure.title('Test01: Verify Login OrangeHrm')
    @allure.description('this test verifies a successful login to OrangeHrm')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebFlows.verify_OrangeHrm_title('Dashboard')

    @allure.title('Test02: Verify Upper Menu Buttons')
    @allure.description('this test verifies upper menu buttons are displayed')
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertions()

    @allure.title('Test03: Create New Employee')
    @allure.description('this test creates a new employee')
    def test_create_employee(self):
        WebFlows.open_pim()
        WebFlows.create_employee('ido', 'orenshtein')
        WebFlows.create_employee('may', 'orenshtein')

    @allure.title('Test04: Verify Employees')
    @allure.description('this test verify employees')
    @pytest.mark.parametrize('search_value,expected', web_flows.testdata)
    def test_verify_employee_csv(self, search_value, expected):
        WebFlows.open_pim()
        WebFlows.verify_employee_csv(search_value, expected)

    @allure.title('Test05: Delete Employee')
    @allure.description('this test deleted employee')
    def test_deleted_employee_card(self):
        WebFlows.open_pim()
        WebFlows.delete_employee_card('ido orenshtein')
        WebFlows.delete_employee_card('may orenshtein')

    def teardown_method(self):
        WebFlows.home(self)
