import re
from model.contact import Contact


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
        wd.find_element_by_xpath("//input[@name='submit'][2]").click()
        self.contact_cache = None

    def details_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def open_details(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='view.php?id=%s']" % contact_id).click()

    def edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def modify(self, id, contact):
        wd = self.app.wd
        # click edit image-button
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_form(contact)
        # submit contact changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete(self, id):
        wd = self.app.wd
        self.app.select_grid_item_by_id(id)
        # click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.app.ensure_confirm_page("Record successful deleted")
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_css_selector("td:nth-child(1) > input").get_attribute("id")
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                address1 = element.find_element_by_css_selector("td:nth-child(4)").text
                emails = element.find_element_by_css_selector("td:nth-child(5)").text
                phones = element.find_element_by_css_selector("td:nth-child(6)").text
                self.contact_cache.append(Contact(id=id, fname=first_name, lname=last_name, address1=address1,
                                                  emails=emails, phones=phones))
        return list(self.contact_cache)

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address1 = wd.find_element_by_name("address").text
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, lname=lastname, fname=firstname, address1=address1, email1=email1, email2=email2,
                       email3=email3, hphone=homephone, mphone=mobilephone, wphone=workphone, hphone2=secondphone)

    def get_info_from_details_page(self, index):
        wd = self.app.wd
        self.details_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Contact(hphone=homephone, mphone=mobilephone, wphone=workphone, hphone2=secondphone)

    def link_to_group(self, contact, group):
        wd = self.app.wd
        self.app.select_grid_item_by_id(contact.id)
        self.app.update_dropdown_field("to_group", group.id)
        wd.find_element_by_name("add").click()
        self.app.ensure_confirm_page("Users added.")

    def details_has_group(self, contact, group):
        wd = self.app.wd
        self.app.navigation.go_home()
        self.open_details(contact.id)
        return wd.find_element_by_xpath("//a[@href='./index.php?group=%s']" % group.id).text == group.name

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (re.sub("[() -]", "", x) for x in
                                 filter(lambda x: x is not None,
                                        [contact.hphone, contact.mphone, contact.wphone, contact.hphone2]))))

    def merge_emails(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3])))

    def strip_spaces(self, contact):
        contact.fname = ' '.join(contact.fname.split())
        contact.lname = ' '.join(contact.lname.split())
        contact.address1 = ' '.join(contact.address1.split())
        contact.email1 = ' '.join(contact.email1.split())
        contact.email2 = ' '.join(contact.email2.split())
        contact.email3 = ' '.join(contact.email3.split())
        return contact

    def make_emails_and_phones(self, contact):
        contact.emails = self.merge_emails(contact)
        contact.phones = self.merge_phones(contact)
        return contact

    def ensure_existence_sanity_check(self, db):
        self.app.navigation.go_home()
        if len(db.get_contact_list()) == 0:
            self.app.contact.create(Contact(fname="Safety Contact"))
            self.app.navigation.go_home()
