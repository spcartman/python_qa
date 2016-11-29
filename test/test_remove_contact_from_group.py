# -*- coding: utf-8 -*-


def test_link_contact_to_group(app, db, orm, check_ui):
    app.contact.ensure_existence_sanity_check(db)
    app.group.ensure_existence_sanity_check(db)