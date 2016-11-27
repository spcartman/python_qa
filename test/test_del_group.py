# -*- coding: utf-8 -*-
from random import choice
from model.group import Group


def test_del_group(app, db):
    app.navigation.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Safety Group"))
        app.navigation.open_groups_page()
    old_groups = db.get_group_list()
    group_to_delete = choice(old_groups)
    app.group.delete(group_to_delete.id)
    old_groups.remove(group_to_delete)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
