import allure
import pytest

from utilities.common_ops import Save, Direction
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class Test_Mobile:
    @allure.title('Test01: Verify Mortgage Repayment')
    @allure.description('this test verifies the mortgage repayment')
    def test_verify_repayment(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.No)
        MobileFlows.verify_mortgage_repayment('17.94')

    @allure.title('Test02: Verify Saved Details')
    @allure.description('this test verifies saved transaction details')
    def test_saved_details(self):
        MobileFlows.mortgage_flow('5000', '8', '3', Save.Yes)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_rate_delete_transaction('3.0')
