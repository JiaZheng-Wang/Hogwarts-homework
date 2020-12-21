# @Time    : 2020/12/20 18:07
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from homework.test_web_weixin.page.base_page import BasePage



class AddPartyPage(BasePage):
    _loc_name = (By.CSS_SELECTOR, ".ww_inputText[name='name']")
    _loc_party_list = (By.CSS_SELECTOR, ".js_toggle_party_list span.ww_btn_Dropdown_arrow")
    _loc_commit = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.ww_btn_Blue[d_ck='submit']")

    def select_party(self, name):
        self.element = self.driver.find_element(by=By.XPATH,
                                                value=f"//form//a[@class='jstree-anchor' and text()='{name}']")
        return self.element

    def add_party(self, name):
        from homework.test_web_weixin.page.contact_page import ContactPage
        self.find(self._loc_name).send_keys(name)
        self.find(self._loc_party_list).click()
        self.select_party("测试小站").click()
        self.find(self._loc_commit).click()
        sleep(2)
        return ContactPage(self.driver).get_party_list()

    def add_party_fail(self):
        pass
