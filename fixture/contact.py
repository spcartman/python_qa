from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def select(self):
        # TODO: implement proper selection, currently function deletes first contact only
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_text_field(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def update_dropdown_field(self, field, value):
        wd = self.app.wd
        if value is not None:
            item = Select(wd.find_element_by_name(field))
            item.select_by_value(value)

    def fill_form(self, contact):
        # TODO: merge update test and dropdown fields, merge fill_form and set_group methods
        self.update_text_field("firstname", contact.fname)
        self.update_text_field("middlename", contact.mname)
        self.update_text_field("lastname", contact.lname)
        self.update_text_field("nickname", contact.nick)
        self.update_text_field("title", contact.title)
        self.update_text_field("company", contact.company)
        self.update_text_field("address", contact.address1)
        self.update_text_field("home", contact.hphone)
        self.update_text_field("mobile", contact.mphone)
        self.update_text_field("work", contact.wphone)
        self.update_text_field("fax", contact.fax)
        self.update_text_field("email", contact.email1)
        self.update_text_field("email2", contact.email2)
        self.update_text_field("email3", contact.email3)
        self.update_text_field("homepage", contact.homepage)
        self.update_dropdown_field("bday", contact.bday)
        self.update_dropdown_field("bmonth", contact.bmonth)
        self.update_text_field("byear", contact.byear)
        self.update_dropdown_field("aday", contact.aday)
        self.update_dropdown_field("amonth", contact.amonth)
        self.update_text_field("ayear", contact.ayear)
        self.update_text_field("address2", contact.address2)
        self.update_text_field("phone2", contact.hphone2)
        self.update_text_field("notes", contact.notes)

    def set_group(self, contact):
        wd = self.app.wd
        new_group = Select(wd.find_element_by_name("new_group"))
        new_group.select_by_index(contact.group)

    def create(self, contact):
        wd = self.app.wd
        # open contact creation form
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        self.set_group(contact)
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
        self.select()
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
