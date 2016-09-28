# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from navigation import Navigation
from login import Auth


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        Navigation().open_home_page(wd)
        Auth().login(wd, username="admin", password="secret")
        Navigation().open_groups_page(wd)
        self.create_group(wd, Group(name="group_002", header="another_header", footer="another_footer"))
        Navigation().open_groups_page(wd)
        Auth().logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        Navigation().open_home_page(wd)
        Auth().login(wd, username="admin", password="secret")
        Navigation().open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        Navigation().open_groups_page(wd)
        Auth().logout(wd)

    def create_group(self, wd, group):
        # open group creation form
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
