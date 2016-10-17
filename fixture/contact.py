class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        wd = self.app.wd
        self.app.update_text_field("firstname", contact.fname)
        self.app.update_text_field("middlename", contact.mname)
        self.app.update_text_field("lastname", contact.lname)
        self.app.update_text_field("nickname", contact.nick)
        self.app.update_text_field("title", contact.title)
        self.app.update_text_field("company", contact.company)
        self.app.update_text_field("address", contact.address1)
        self.app.update_text_field("home", contact.hphone)
        self.app.update_text_field("mobile", contact.mphone)
        self.app.update_text_field("work", contact.wphone)
        self.app.update_text_field("fax", contact.fax)
        self.app.update_text_field("email", contact.email1)
        self.app.update_text_field("email2", contact.email2)
        self.app.update_text_field("email3", contact.email3)
        self.app.update_text_field("homepage", contact.homepage)
        self.app.update_dropdown_field("bday", contact.bday)
        self.app.update_dropdown_field("bmonth", contact.bmonth)
        self.app.update_text_field("byear", contact.byear)
        self.app.update_dropdown_field("aday", contact.aday)
        self.app.update_dropdown_field("amonth", contact.amonth)
        if len(wd.find_elements_by_name("new_group")) > 0:
            self.app.update_dropdown_field("new_group", contact.group)
        self.app.update_text_field("ayear", contact.ayear)
        self.app.update_text_field("address2", contact.address2)
        self.app.update_text_field("phone2", contact.hphone2)
        self.app.update_text_field("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        # open contact creation form
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify(self, contact):
        wd = self.app.wd
        # click edit image-button
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_form(contact)
        # submit contact changes
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.app.wd
        self.app.select_item()
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
