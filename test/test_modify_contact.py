# -*- coding: utf-8 -*-
from random import choice
from model.contact import Contact


def test_modify_contact(app, db, data_contacts):
    contact = data_contacts
    app.navigation.go_home()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = db.get_contact_list()
    contact_to_modify = choice(old_contacts)
    contact.id = contact_to_modify.id
    app.contact.modify(contact_to_modify.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_modify)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
