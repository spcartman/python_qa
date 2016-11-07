# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_modify_whole_contact(app, data_contacts):
    contact = data_contacts
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify(index, contact)
    app.navigation.go_home()
    assert len(old_contacts) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
