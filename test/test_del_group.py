# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="Safety Group"))
    app.group.delete()
    app.navigation.open_groups_page()
