# -*- coding: utf-8 -*-
from random import choice
from model.group import Group


def test_modify_group(app, db, data_groups, check_ui):
    group = data_groups
    app.group.ensure_existence_sanity_check(db)
    app.navigation.open_groups_page()
    old_groups = db.get_group_list()
    group_to_modify = choice(old_groups)
    group.id = group_to_modify.id
    app.group.modify(group_to_modify.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_modify)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        app.navigation.open_groups_page()
        assert sorted(map(app.group.strip_spaces, new_groups),
                      key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
