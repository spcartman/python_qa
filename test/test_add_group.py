# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

test_data = [Group(name=name, header=header, footer=footer)
             for name in ("", rand_string("name", 10))
             for header in ("", rand_string("header", 20))
             for footer in ("", rand_string("footer", 20))]


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
