# -*- coding: utf-8 -*-


def test_del_group(app):
    app.navigation.open_groups_page()
    app.group.delete()
    app.navigation.open_groups_page()
