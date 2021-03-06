# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_random_contact_info_on_home_page(app, db):
    app.contact.ensure_existence_sanity_check(db)
    app.navigation.go_home()
    index = randrange(len(app.contact.get_contact_list()))
    contact_home_page = app.contact.get_contact_list()[index]
    contact_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_home_page.lname == contact_edit_page.lname
    assert contact_home_page.fname == contact_edit_page.fname
    assert contact_home_page.address1 == contact_edit_page.address1
    assert contact_home_page.emails == app.contact.merge_emails(contact_edit_page)
    assert contact_home_page.phones == app.contact.merge_phones(contact_edit_page)


def test_home_page_info(app, db):
    app.navigation.go_home()
    assert sorted(map(app.contact.make_emails_and_phones,
                      map(app.contact.strip_spaces,
                          db.get_contact_list())),
                  key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_info_on_details_page(app):
#     app.navigation.go_home()
#     contact_info_page = app.contact.get_info_from_details_page(3)
#     app.navigation.go_home()
#     contact_edit_page = app.contact.get_info_from_edit_page(3)
#     # assert contact_info_page.lname == contact_edit_page.lname
#     # assert contact_info_page.fname == contact_edit_page.fname
#     # assert contact_info_page.address1 == contact_edit_page.address1
#     # assert contact_info_page.email1 == contact_edit_page.email1
#     # assert contact_info_page.email2 == contact_edit_page.email2
#     # assert contact_info_page.email3 == contact_edit_page.email3
#     assert contact_info_page.hphone == contact_edit_page.hphone
#     assert contact_info_page.mphone == contact_edit_page.mphone
#     assert contact_info_page.wphone == contact_edit_page.wphone
#     assert contact_info_page.hphone2 == contact_edit_page.hphone2
