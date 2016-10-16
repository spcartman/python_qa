# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.open_groups_page()
    app.group.create(Group(name="group_002", header="another_header", footer="another_footer"))
    app.navigation.open_groups_page()


def test_add_empty_group(app):
    app.navigation.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.navigation.open_groups_page()
