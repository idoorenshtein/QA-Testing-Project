from selenium.webdriver.common.by import By

OpenMenu = (By.CSS_SELECTOR, "button[role='none']")
Search = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
Admin = (By.CSS_SELECTOR, 'a[href="/web/index.php/admin/viewAdminModule"]')
PIM = (By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]')
Leave = (By.CSS_SELECTOR, 'a[href="/web/index.php/leave/viewLeaveModule"]')
Time = (By.CSS_SELECTOR, 'a[href="/web/index.php/time/viewTimeModule"]')
Recruitment = (By.CSS_SELECTOR, 'a[href="/web/index.php/recruitment/viewRecruitmentModule"]')
MyInfo = (By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewMyDetails"]')
Performance = (By.CSS_SELECTOR, 'a[href="/web/index.php/performance/viewPerformanceModule"]')
Dashboard = (By.CSS_SELECTOR, 'a[href="/web/index.php/dashboard/index"]')
Directory = (By.CSS_SELECTOR, 'a[href="/web/index.php/directory/viewDirectory"]')
Maintenance = (By.CSS_SELECTOR, 'a[href="/web/index.php/maintenance/viewMaintenanceModule"]')
Buzz = (By.CSS_SELECTOR, 'a[href="/web/index.php/buzz/viewBuzz"]')


class LeftMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_OpenMenu(self):
        return self.driver.find_element(OpenMenu[0], OpenMenu[1])

    def get_Search(self):
        return self.driver.find_element(Search[0], Search[1])

    def get_Admin(self):
        return self.driver.find_element(Admin[0], Admin[1])

    def get_PIM(self):
        return self.driver.find_element(PIM[0], PIM[1])

    def get_Leave(self):
        return self.driver.find_element(Leave[0], Leave[1])

    def get_Time(self):
        return self.driver.find_element(Time[0], Time[1])

    def get_Recruitment(self):
        return self.driver.find_element(Recruitment[0], Recruitment[1])

    def get_My_Info(self):
        return self.driver.find_element(MyInfo[0], MyInfo[1])

    def get_Performance(self):
        return self.driver.find_element(Performance[0], Performance[1])

    def get_Dashboard(self):
        return self.driver.find_element(Dashboard[0], Dashboard[1])

    def get_Directory(self):
        return self.driver.find_element(Directory[0], Directory[1])

    def get_Maintenance(self):
        return self.driver.find_element(Maintenance[0], Maintenance[1])

    def get_Buzz(self):
        return self.driver.find_element(Buzz[0], Buzz[1])
