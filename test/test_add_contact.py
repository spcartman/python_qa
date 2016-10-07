# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login('admin', 'secret')
    app.create_contact(Contact(fname="First Name 001", mname="Middle Name", lname="Last Name 001",
                                nick="fooname", title="Mr.", company="MacroSoft", address1="6, Wood road 19",
                                hphone="185 83 71", mphone="378 74 28", wphone="479 82 21", fax="877 63 76",
                                email1="foo@mail.coom", email2="foo2@mail.coom", email3="foo3@mail.com",
                                homepage="http://localhost/", bday="18", bmonth="July", byear="1981", aday="7",
                                amonth="October", ayear="1983", group=6, address2="8, Home ave 24",
                                hphone2="785 23 67", notes="The contact is created by the script."))
    app.logout()