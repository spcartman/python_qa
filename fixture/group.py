class GroupHelper:

    def __init__(self, app):
        self.app = app

    def select(self):
        # TODO: implement proper selection, currently function selects first group only
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_field(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def fill_form(self, group):
        self.update_field("group_name", group.name)
        self.update_field("group_header", group.header)
        self.update_field("group_footer", group.footer)

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
