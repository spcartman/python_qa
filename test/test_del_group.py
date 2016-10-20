# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete()
    app.navigation.open_groups_page()
    assert (len(old_groups) - 1) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
