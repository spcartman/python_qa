from pytest_bdd import given, when, then
from model.group import Group
from random import choice


@given("a group list")
def group_list(db):
    return db.get_group_list()


@given("new group data <name>, <header> and <footer>")
@given("a group with <name>, <header> and <footer>")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@given("a non-empty group list")
def non_empty_group_list(app, db):
    app.group.ensure_existence_sanity_check(db)
    return db.get_group_list()


@given("a random group from the list")
def random_group(non_empty_group_list):
    return choice(non_empty_group_list)


@when("I add the group to the list")
def add_group(app, new_group):
    app.navigation.open_groups_page()
    app.group.create(new_group)


@when("I modify the group with new data")
def modify_group(app, random_group, new_group):
    app.navigation.open_groups_page()
    new_group.id = random_group.id
    app.group.modify(random_group.id, new_group)


@when("I delete the group from the list")
def delete_group(app, random_group):
    app.navigation.open_groups_page()
    app.group.delete(random_group.id)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    old_groups.append(new_group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@then("the new group list is equal to the old list with the modified group")
def verify_group_modified(db, non_empty_group_list, random_group, new_group):
    old_groups = non_empty_group_list
    old_groups.remove(random_group)
    old_groups.append(new_group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@then("the new group list is equal to the old list without the deleted group")
def verify_group_deleted(db, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    old_groups.remove(random_group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
