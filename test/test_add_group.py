# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group_002", header="another_header", footer="another_footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
