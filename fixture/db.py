import mysql.connector
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
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address, email, email2, email3, home, mobile, work, phone2"
                           " FROM `addressbook` WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, lname, fname, address1, email1, email2, email3, hphone, mphone, wphone, hphone2) = row
                contact_list.append(Contact(id=id, fname=fname, lname=lname, address1=address1))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
