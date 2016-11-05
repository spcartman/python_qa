# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.group import const as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    app.navigation.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    app.navigation.open_groups_page()
    assert (len(old_groups) + 1) == app.count_item()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
