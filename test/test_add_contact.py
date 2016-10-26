# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

test_data = [Contact()] + [Contact(fname=rand_string("fname", 10), lname=rand_string("lname", 10),
                                   address1=rand_string("address", 30), hphone=rand_string("homeph", 10),
                                   mphone=rand_string("mobileph", 10), email1=rand_string("email1", 15))
                           for i in range(2)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    app.navigation.go_home()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.navigation.go_home()
    assert (len(old_contacts) + 1) == app.count_item()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
