from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(6)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def select_item(self):
        # TODO: implement proper selection, currently function deletes first item only
        self.wd.find_element_by_name("selected[]").click()

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
                item.select_by_index(value)
            else:
                item.select_by_value(value)

    def destroy(self):
        self.wd.quit()
