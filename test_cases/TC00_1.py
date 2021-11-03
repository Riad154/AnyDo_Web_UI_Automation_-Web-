import unittest
from selenium import webdriver
from pages.Create_Task import CreateTask
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")


class TestAnyDo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\\Education\\Python\\New folder\\chromedriver_win32\\chromedriver.exe", options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "https://desktop.any.do/"


    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def test_TC00_1(self):
        driver = self.driver
        driver.get(self.base_url)
        CT = CreateTask(driver)
        CT.click_task()
        CT.insert_want_to("My Daily Task")
        time.sleep(2)
        CT.add_task()
        time.sleep(2)




if __name__ == " __main__":
    unittest.main()