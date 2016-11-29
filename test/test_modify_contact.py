# -*- coding: utf-8 -*-
from random import choice
from model.contact import Contact


def test_modify_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    app.contact.ensure_existence_sanity_check(db)
    old_contacts = db.get_contact_list()
    contact_to_modify = choice(old_contacts)
    contact.id = contact_to_modify.id
    app.contact.modify(contact_to_modify.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_modify)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        app.navigation.go_home()
        assert sorted(map(app.contact.strip_spaces, new_contacts),
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
