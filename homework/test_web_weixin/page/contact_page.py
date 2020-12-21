# @Time    : 2020/12/20 18:01
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from selenium.webdriver.common.by import By

from homework.test_web_weixin_2.page.add_party_page import AddPartyPage
from homework.test_web_weixin_2.page.base_page import BasePage


class ContactPage(BasePage):
    _loc_add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _loc_add_party = (By.CSS_SELECTOR, ".js_create_party")
    _loc_party_list = (By.CSS_SELECTOR, ".jstree-anchor")

    def to_add_member(self):
        pass

    def to_add_party(self):
        # self.wait_to_click(self._loc_add)
        self.find(self._loc_add).click()
        self.find(self._loc_add_party).click()
        return AddPartyPage(self.driver)

    def get_party_list(self):
        # 返回部门名称的列表
        return [element.text for element in self.finds(self._loc_party_list)]
