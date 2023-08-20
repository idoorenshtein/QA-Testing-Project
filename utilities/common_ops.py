import csv
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


# This function reads data from external xml file
def get_data(node_name):
    root = ET.parse('C:/Automation/test_automation_Final_Project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


# This function waits until the element is displayed or exists
def wait(for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))


# This function reads data from a csv file and returns the data as a list
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


def get_time_stamp():
    return time.time()


# Enum for Selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'


# Enum for selecting whether we want to save mortgage transaction or not
class Save:
    Yes = True
    No = False


# Enum for selecting whether we want to save mortgage transaction or not
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
