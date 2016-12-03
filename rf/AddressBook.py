import json
import os.path
from random import choice
from model.group import Group
from model.contact import Contact
from fixture.application import Application
from fixture.db import DBFixture


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        self.dbfixture = DBFixture(host=self.target["db"]["host"], db_name=self.target["db"]["db_name"],
                                   user=self.target["db"]["user"], password=self.target["db"]["pass"])
        self.fixture = Application(browser=self.browser, base_url=self.target["web"]["baseUrl"])
        self.fixture.navigation.open_home_page()
        self.fixture.session.ensure_login(username=self.target["web"]["username"],
                                          password=self.target["web"]["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def random_entity(self, entity_list):
        return choice(entity_list)

    def create_group(self, group):
        self.fixture.navigation.open_groups_page()
        self.fixture.group.create(group)

    def modify_group(self, group_to_modify, group):
        self.fixture.navigation.open_groups_page()
        group.id = group_to_modify.id
        self.fixture.group.modify(group_to_modify.id, group)

    def delete_group(self, group):
        self.fixture.navigation.open_groups_page()
        self.fixture.group.delete(group.id)

    def ensure_group_exists(self):
        self.fixture.group.ensure_existence_sanity_check(self.dbfixture)

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def group_lists_equal(self, old_groups, new_groups):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def create_contact(self, contact):
        self.fixture.navigation.go_home()
        self.fixture.contact.create(contact)

    def modify_contact(self, contact_to_modify, contact):
        self.fixture.navigation.go_home()
        contact.id = contact_to_modify.id
        self.fixture.contact.modify(contact_to_modify.id, contact)

    def delete_contact(self, contact):
        self.fixture.navigation.go_home()
        self.fixture.contact.delete(contact.id)

    def ensure_contact_exists(self):
        self.fixture.contact.ensure_existence_sanity_check(self.dbfixture)

    def new_contact(self, first_name, last_name, address, mobile_phone, email):
        return Contact(fname=first_name, lname=last_name, address1=address, mphone=mobile_phone, email1=email)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def contact_lists_equal(self, old_contacts, new_contacts):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
