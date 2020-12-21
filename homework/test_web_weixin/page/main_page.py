# @Time    : 2020/12/20 18:00
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from selenium.webdriver.common.by import By

from homework.test_web_weixin_2.page.add_member_page import AddMemberPage
from homework.test_web_weixin_2.page.base_page import BasePage
from homework.test_web_weixin_2.page.contact_page import ContactPage


class MainPage(BasePage):

    def to_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def to_add_member(self):
        return AddMemberPage(self.driver)
