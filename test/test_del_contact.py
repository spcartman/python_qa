# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.navigation.go_home()
    if app.count_item() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
    app.contact.delete()
    app.navigation.open_home_page()
