class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, group):
        self.app.update_text_field("group_name", group.name)
        self.app.update_text_field("group_header", group.header)
        self.app.update_text_field("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        # open group creation form
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def modify(self, group):
        wd = self.app.wd
        self.app.select_item()
        # click button to edit
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        # submit group changes
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.app.wd
        self.app.select_item()
        wd.find_element_by_name("delete").click()
