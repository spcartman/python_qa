# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_modify_whole_group(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='modified name', header='modified header', footer='modified footer')
    group.id = old_groups[index].id
    app.group.modify(index, group)
    app.navigation.open_groups_page()
    assert len(old_groups) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    app.navigation.open_groups_page()
    if app.count_item() == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='just updated name')
    group.id = old_groups[index].id
    app.group.modify(index, group)
    app.navigation.open_groups_page()
    assert len(old_groups) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
