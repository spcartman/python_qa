# -*- coding: utf-8 -*-


def test_del_contact(app):
    app.navigation.go_home()
    app.contact.delete()
    app.navigation.open_home_page()
