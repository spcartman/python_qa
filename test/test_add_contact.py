# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.navigation.go_home()
    assert (len(old_contacts) + 1) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
