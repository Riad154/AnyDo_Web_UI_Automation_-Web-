
from selenium.webdriver.common.keys import Keys



class CreateTask:
    def __init__(self, driver):
        self.driver = driver


    def click_task(self):
        return self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/div[2]/div/button/span[2]').click()

    def insert_want_to(self, Task):
        return self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[1]/div/div/div/textarea").send_keys(Task)

    def insert_notes(self, Task2):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea').send_keys(Task2)
    def click_next_week(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[3]/div[2]/div[2]/button[2]').click()

    def add_task(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button').click()

    def click_My_Friday_Task(self):
        return self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/section/div/article[1]/div/div[1]/article/div/div[1]/div/div/div/div[1]/div[1]/div[1]').click()

    def insert_sub_task(self, Task3):
        return self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/div/div/div[1]/input").send_keys(Task3)

    def press_enter(self):
        return self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/div/div/div[1]/input").send_keys(Keys.ENTER)









