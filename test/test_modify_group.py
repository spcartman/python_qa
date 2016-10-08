# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.navigation.open_groups_page()
    app.group.modify(Group(name='modif name', header='modif header', footer='modif footer'))
    app.navigation.open_groups_page()
    app.session.logout()
