# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    app.navigation.go_home()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    old_contacts.append(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        app.navigation.go_home()
        assert sorted(map(app.contact.strip_spaces, new_contacts),
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
