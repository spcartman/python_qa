# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_del_group(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    app.navigation.open_groups_page()
    assert (len(old_groups) - 1) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
