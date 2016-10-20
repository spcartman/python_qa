# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_whole_group(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name='modified name', header='modified header', footer='modified footer')
    group.id = old_groups[0].id
    app.group.modify(group)
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name='just updated name')
    group.id = old_groups[0].id
    app.group.modify(group)
    app.navigation.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)