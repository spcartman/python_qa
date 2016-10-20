# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="First Name 005", mname="Middle Name", lname="Last Name 005", nick="fooname",
                      title="Mr.", company="MacroSoft", address1="6, Wood road 19", hphone="185 83 71",
                      mphone="378 74 28", wphone="479 82 21", fax="877 63 76", email1="foo@mail.coom",
                      email2="foo2@mail.coom", email3="foo3@mail.com", homepage="http://localhost/", bday="18",
                      bmonth="July", byear="1981", aday="7", amonth="October", ayear="1983", group=6,
                      address2="8, Home ave 24", hphone2="785 23 67", notes="The contact is created by the script.")
    app.contact.create(contact)
    app.navigation.go_home()
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
