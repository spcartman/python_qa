# -*- coding: utf-8 -*-
from random import randrange


def test_info_on_home_page(app):
    app.navigation.go_home()
    index = randrange(len(app.contact.get_contact_list()))
    contact_home_page = app.contact.get_contact_list()[index]
    contact_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_home_page.lname == contact_edit_page.lname
    assert contact_home_page.fname == contact_edit_page.fname
    assert contact_home_page.address1 == contact_edit_page.address1
    assert contact_home_page.emails == app.contact.merge_emails(contact_edit_page)
    assert contact_home_page.phones == app.contact.merge_phones(contact_edit_page)


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
