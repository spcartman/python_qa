# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, data_group):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(data_group)
    app.navigation.open_groups_page()
    assert (len(old_groups) + 1) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups.append(data_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
