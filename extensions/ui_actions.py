import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf


class UiActions:
    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('updating text')
    def Update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover tooltip')
    def mouse_hover_tooltip(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step('mouse hover two element')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('right click on element')
    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step('drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step('clear text field in element')
    def clear(elem: WebElement):
        elem.clear()