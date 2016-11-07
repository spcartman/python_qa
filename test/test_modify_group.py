# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_modify_whole_group(app, json_groups):
    group = json_groups
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify(index, group)
    app.navigation.open_groups_page()
    assert len(old_groups) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
