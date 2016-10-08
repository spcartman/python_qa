class GroupHelper:

    def __init__(self, app):
        self.app = app

    def select(self):
        # TODO: implement proper selection, currently function selects first group only
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        # open group creation form
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def modify(self, group):
        wd = self.app.wd
        # select group for edit
        self.select()
        # click button to edit
        wd.find_element_by_name("edit").click()
        # make changes to group fields
        self.fill_form(group)
        # submit group changes
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.app.wd
        self.select()
        wd.find_element_by_name("delete").click()
