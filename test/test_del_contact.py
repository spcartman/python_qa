# -*- coding: utf-8 -*-


def test_del_contact(app):
    app.navigation.open_home_page()
    app.session.login('admin', 'secret')
    app.contact.delete()
    app.navigation.open_home_page()
    app.session.logout()
