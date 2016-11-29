# -*- coding: utf-8 -*-
from random import choice
from model.group import Group


def test_del_group(app, db, check_ui):
    app.group.ensure_existence_sanity_check(db)
    old_groups = db.get_group_list()
    group_to_delete = choice(old_groups)
    app.group.delete(group_to_delete.id)
    old_groups.remove(group_to_delete)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        app.navigation.open_groups_page()
        assert sorted(map(app.group.strip_spaces, new_groups),
                      key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
