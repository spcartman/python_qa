from pytest_bdd import given, when, then
from model.contact import Contact
from random import choice


@given("a contact list")
def contact_list(db):
    return db.get_contact_list()


@given("new contact data <first_name>, <last_name>, <address>, <mobile_phone> and <email>")
@given("a contact with <first_name>, <last_name>, <address>, <mobile_phone> and <email>")
def new_contact(first_name, last_name, address, mobile_phone, email):
    return Contact(fname=first_name, lname=last_name, address1=address, mphone=mobile_phone, email1=email)


@given("a non-empty contact list")
def non_empty_contact_list(app, db):
    app.contact.ensure_existence_sanity_check(db)
    return db.get_contact_list()


@given("a random contact from the list")
def random_contact(non_empty_contact_list):
    return choice(non_empty_contact_list)


@when("I add the contact to the list")
def add_contact(app, new_contact):
    app.navigation.go_home()
    app.contact.create(new_contact)


@when("I modify the contact with new data")
def modify_contact(app, random_contact, new_contact):
    app.navigation.go_home()
    new_contact.id = random_contact.id
    app.contact.modify(random_contact.id, new_contact)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.navigation.go_home()
    app.contact.delete(random_contact.id)


@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    old_contacts.append(new_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then("the new contact list is equal to the old list with the modified contact")
def verify_contact_modified(db, non_empty_contact_list, random_contact, new_contact):
    old_contacts = non_empty_contact_list
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    old_contacts.remove(random_contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
