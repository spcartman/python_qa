# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_whole_group(app):
    app.navigation.open_groups_page()
    app.group.modify(Group(name='modified name', header='modified header', footer='modified footer'))
    app.navigation.open_groups_page()


def test_modify_group_name(app):
    app.navigation.open_groups_page()
    app.group.modify(Group(name='just updated name'))
    app.navigation.open_groups_page()
