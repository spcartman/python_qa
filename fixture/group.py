from model.group import Group


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
        self.group_cache = None

    def modify(self, id, group):
        wd = self.app.wd
        self.app.select_grid_item_by_id(id)
        # click button to edit
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        # submit group changes
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def delete(self, id):
        wd = self.app.wd
        self.app.select_grid_item_by_id(id)
        wd.find_element_by_name("delete").click()
        self.app.ensure_confirm_page("Group has been removed.")
        self.group_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                name = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name, id=id))
        return list(self.group_cache)

    def strip_spaces(self, group):
        group.name = ' '.join(group.name.split())
        return group

    def ensure_existence_sanity_check(self, db):
        if len(db.get_group_list()) == 0:
            db.insert_sanity_group()
