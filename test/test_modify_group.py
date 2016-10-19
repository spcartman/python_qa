# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_whole_group(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.modify(Group(name='modified name', header='modified header', footer='modified footer'))
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    app.group.modify(Group(name='just updated name'))
    app.navigation.open_groups_page()
