# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete()
    app.navigation.go_home()
    assert (len(old_contacts) - 1) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
