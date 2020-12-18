# @Time    : 2020/12/18 10:59
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from homework.BasePage import PageBase


class PageWx(PageBase):

    # loc_menu_contacts = (By.CSS_SELECTOR, "#menu_contacts span")
    # loc_add_contacts = (By.CSS_SELECTOR, "span.index_service_cnt_item_title")
    # todo：支持传参，添加按条件搜索的方法进行断言，目前默认取第一页
    def add_contacts(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.driver.find_element(By.ID, "username").send_keys("王小二")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("xiaoer")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("xiaoer_wang")

        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("test_daikuan1@163.com")
        self.driver.find_element(By.CSS_SELECTOR, ".member_edit_sec:nth-child(2)").click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("测试总监")
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()

        contact_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td span")
        text_list = []

        # 查出列表所有text并返回
        for i in contact_list:
            text_list.append(i.text)
        return text_list
