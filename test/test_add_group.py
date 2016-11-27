# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, data_groups, check_ui):
    group = data_groups
    app.navigation.open_groups_page()
    old_groups = db.get_group_list()
    app.group.create(group)
    old_groups.append(group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        app.navigation.open_groups_page()
        assert sorted(map(app.group.strip_spaces, new_groups),
                      key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
