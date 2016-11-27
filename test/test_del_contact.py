# -*- coding: utf-8 -*-
from random import choice
from model.contact import Contact
from time import sleep


def test_del_contact(app, db, check_ui):
    app.navigation.go_home()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = db.get_contact_list()
    contact_to_delete = choice(old_contacts)
    app.contact.delete(contact_to_delete.id)
    old_contacts.remove(contact_to_delete)
    sleep(1)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        app.navigation.go_home()
        assert sorted(map(app.contact.strip_spaces, new_contacts),
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
