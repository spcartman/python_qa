# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
        app.navigation.go_home()
    app.contact.delete()
    app.navigation.go_home()
