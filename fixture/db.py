import mysql.connector
from random import choice
from model.group import Group
from model.contact import Contact


class DBFixture:

    def __init__(self, host, db_name, user, password):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=db_name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            return self.cursor_to_model_group(cursor)
        finally:
            cursor.close()

    def get_contact_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2"
                           " FROM addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            return self.cursor_to_model_contact(cursor)
        finally:
            cursor.close()

    def get_group_by_id(self, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list"
                           " WHERE group_id = %s" % group_id)
            return self.cursor_to_model_group(cursor)[0]
        finally:
            cursor.close()

    def get_contact_by_id(self, contact_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2"
                           " FROM addressbook WHERE deprecated = '0000-00-00 00:00:00' AND id = %s" % contact_id)
            return self.cursor_to_model_contact(cursor)[0]
        finally:
            cursor.close()

    def cursor_to_model_group(self, cursor):
        group_list = []
        for row in cursor:
            (id, name, header, footer) = row
            group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        return group_list

    def cursor_to_model_contact(self, cursor):
        contact_list = []
        for row in cursor:
            (id, lname, fname, address1, email1, email2, email3, hphone, mphone, wphone, hphone2) = row
            contact_list.append(Contact(id=str(id), fname=fname, lname=lname, address1=address1,
                                        email1=email1, email2=email2, email3=email3,
                                        hphone=hphone, mphone=mphone, wphone=wphone, hphone2=hphone2))
        return contact_list

    def insert_sanity_group(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO group_list(group_name) VALUES ('Sanity Group via DB')")
        finally:
            cursor.close()

    def insert_sanity_contact(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO addressbook(firstname) VALUES ('Sanity Contact via DB')")
        finally:
            cursor.close()

    def get_random_linked_pair(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, id FROM address_in_groups")
            for row in cursor:
                group_list.append((row[0], row[1]))
        finally:
            cursor.close()
        if len(group_list) > 0:
            pair = choice(group_list)
            return self.get_group_by_id(pair[0]), self.get_contact_by_id(pair[1])
        return None

    def destroy(self):
        self.connection.close()
