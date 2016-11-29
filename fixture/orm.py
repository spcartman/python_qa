from datetime import datetime
from pony.orm import *
from pymysql.converters import decoders
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")

    def __init__(self, host, db_name, user, password):
        self.db.bind("mysql", host=host, database=db_name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def covert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def covert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), fname=contact.firstname, lname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.covert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.covert_contacts_to_model(select(c for c in ORMFixture.ORMContact
                                                    if c.deprecated is None))
