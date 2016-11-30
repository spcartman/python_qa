# -*- coding: utf-8 -*-
from random import choice


def test_link_contact_to_group(app, db, orm, check_ui):
    app.group.ensure_existence_sanity_check(db)
    group_to_link = choice(db.get_group_list())
    db.insert_sanity_contact()  # to make sure contact with `group_to_link` unlinked can be selected
    contact_to_link = choice(orm.get_contacts_not_in_group(group_to_link))
    app.navigation.go_home()
    app.contact.link_to_group(contact_to_link, group_to_link)
    assert contact_to_link.id in (c.id for c in orm.get_contacts_in_group(group_to_link))
    if check_ui:
        assert app.contact.details_has_group(contact_to_link, group_to_link)
