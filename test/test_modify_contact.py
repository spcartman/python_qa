# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_whole_contact(app):
    app.navigation.go_home()
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
    app.contact.modify(Contact(fname="New First Name 003", mname="New Middle Name", lname="New Last Name 003",
                               nick="New fooname", title="New Mr.", company="New MacroSoft", address1="6, New road 19",
                               hphone="333 83 33", mphone="333 74 33", wphone="333 82 33", fax="333 63 33",
                               email1="new_foo@mail.coom", email2="new_foo2@mail.coom", email3="new_foo3@mail.com",
                               homepage="http://new_localhost/", bday="22", bmonth="June", byear="1933", aday="11",
                               amonth="april", ayear="1955", group=7, address2="8, New Home ave 24",
                               hphone2="333 23 33", notes="The contact is UPDATED by the script."))
    app.navigation.go_home()


def test_modify_contact_name(app):
    app.navigation.go_home()
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="Safety Contact"))
    app.contact.modify(Contact(fname="New First Name 003"))
    app.navigation.go_home()
