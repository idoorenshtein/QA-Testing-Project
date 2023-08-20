import time

import allure
import pytest

from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_Web_DB:
    @allure.title('Test01: Login to OrangeHrm via DB')
    @allure.description('This test verify login using elements taken from database')
    def test_verify_login_db(self):
        DBFlows.login_orangehrm_via_db()
        WebFlows.verify_OrangeHrm_title('Dashboard')
