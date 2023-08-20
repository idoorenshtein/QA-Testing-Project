import allure
import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures('init_desktop_driver')
class Test_Desktop:
    @allure.title('Test01: Adding 2 Numbers')
    @allure.description('This test adds 2 numbers and verify the result')
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow('1+7')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '8')

    @allure.title('Test02: Arithmetic Actions')
    @allure.description('This test does some arithmetic actions and verifies it')
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flow('2*5+50/2-25')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '5')

    def teardown_method(self):
        DesktopFlows.clear_flow()