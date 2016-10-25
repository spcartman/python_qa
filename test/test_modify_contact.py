# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_modify_whole_contact(app):
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(fname="New First Name 003", mname="New Middle Name", lname="New Last Name 003", nick="Ne fooname",
                      title="New Mr.", company="New MacroSoft", address1="6, New road 19", hphone="333 83 33",
                      mphone="333 74 33", wphone="333 82 33", fax="333 63 33", email1="new_foo@mail.coom",
                      email2="new_foo2@mail.coom", email3="new_foo3@mail.com", homepage="http://new_host/", bday="22",
                      bmonth="June", byear="1933", aday="11", amonth="april", ayear="1955", group=7,
                      address2="8, New Home ave 24", hphone2="333 23 33", notes="The contact is UPDATED by the script.")
    contact.id = old_contacts[index].id
    app.contact.modify(index, contact)
    app.navigation.go_home()
    assert len(old_contacts) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_name(app):
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(fname="Just name change")
    contact.id = old_contacts[index].id
    app.contact.modify(index, contact)
    app.navigation.go_home()
    assert len(old_contacts) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
