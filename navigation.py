class Navigation:
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def return_home(self, wd):
        wd.find_element_by_link_text("home page").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()
