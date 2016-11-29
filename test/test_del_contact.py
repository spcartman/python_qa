# -*- coding: utf-8 -*-
from random import choice
from model.contact import Contact


def test_del_contact(app, db, check_ui):
    app.contact.ensure_existence_sanity_check(db)
    old_contacts = db.get_contact_list()
    contact_to_delete = choice(old_contacts)
    app.contact.delete(contact_to_delete.id)
    old_contacts.remove(contact_to_delete)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        app.navigation.go_home()
        assert sorted(map(app.contact.strip_spaces, new_contacts),
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
