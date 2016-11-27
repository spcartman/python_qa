# -*- coding: utf-8 -*-
from random import choice
from model.contact import Contact
import time


def test_del_contact(app, db):
    app.navigation.go_home()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = db.get_contact_list()
    contact_to_delete = choice(old_contacts)
    app.contact.delete(contact_to_delete.id)
    old_contacts.remove(contact_to_delete)
    time.sleep(1)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
