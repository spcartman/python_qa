# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="group_002", header="another_header", footer="another_footer")
    app.group.create(group)
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1) == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert (len(old_groups) + 1) == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
