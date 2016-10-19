# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group_002", header="another_header", footer="another_footer"))
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1) == len(new_groups)


def test_add_empty_group(app):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    app.navigation.open_groups_page()
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1) == len(new_groups)
