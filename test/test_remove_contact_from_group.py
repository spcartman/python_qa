# -*- coding: utf-8 -*-
from random import choice


def test_remove_contact_from_group(app, db, orm):
    if not db.get_random_linked_pair():
        app.group.ensure_existence_sanity_check(db)
        app.contact.ensure_existence_sanity_check(db)
        group_to_link = choice(db.get_group_list())
        contact_to_link = choice(db.get_contact_list())
        app.navigation.go_home()
        app.contact.link_to_group(contact_to_link, group_to_link)
    app.navigation.go_home()
    group_to_unlink, contact_to_unlink = db.get_random_linked_pair()
    app.contact.unlink_from_group(contact_to_unlink, group_to_unlink)
    assert contact_to_unlink.id not in (c.id for c in orm.get_contacts_in_group(group_to_unlink))
