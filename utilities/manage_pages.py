import test_cases.conftest as conf
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.add_employee_page import AddEmployeePage
from page_objects.web_objects.left_menu_page import LeftMenuPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.pim_page import PimPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from page_objects.web_objects.upper_pim_menu_page import UpperPim

# Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_left_menu = None
web_pim = None
web_upper_pim = None
web_add_employee = None

# Mobile Objects
mobile_calculator = None
mobile_saved = None

# Electron Objects
electron_task = None

# Desktop Objects
standard_calc = None


class MangePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_left_menu'] = LeftMenuPage(conf.driver)
        globals()['web_pim'] = PimPage(conf.driver)
        globals()['web_upper_pim'] = UpperPim(conf.driver)
        globals()['web_add_employee'] = AddEmployeePage(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['standard_calc'] = StandardPage(conf.driver)
