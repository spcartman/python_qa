class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def go_home(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and (len(wd.find_elements_by_name("new")) > 0)):
            wd.find_element_by_link_text("groups").click()
