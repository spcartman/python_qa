from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)
        self.session = SessionHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def select_item_by_index(self, index):
        self.wd.find_elements_by_name("selected[]")[index].click()

    def select_item_by_id(self, id):
        self.wd.find_element_by_xpath("//input[@value='%s']" % id).click()

    def count_item(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def update_text_field(self, field, value):
        if value is not None:
            self.wd.find_element_by_name(field).click()
            self.wd.find_element_by_name(field).clear()
            self.wd.find_element_by_name(field).send_keys(value)

    def update_dropdown_field(self, field, value):
        # TODO: merge update_text and update_dropdown methods
        if value is not None:
            item = Select(self.wd.find_element_by_name(field))
            if field == "new_group":
                # item.select_by_index(value)
                pass  # TODO: check for the number of elements in dropdown
            else:
                item.select_by_value(value)

    def destroy(self):
        self.wd.quit()
