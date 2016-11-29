# import mysql.connector
# import pymysql
# from model.contact import Contact


# conn = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     conn.close()

from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", db_name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="161"))
    for i in l:
        print(i)
    print("\n", len(l))
finally:
    pass

# input_s = '    h    a h  k   k        j  l  '
# output_s = ''
# count = 0
# for i in range(len(input_s)):
#     if input_s[i] == ' ':
#         count += 1
#     else:
#         count = 0
#     if count < 2:
#         output_s += input_s[i]
#
# print('in: ' + input_s + '.')
# print('out: ' + output_s + '.')
# print('better: ' + ' '.join(input_s.split()) + '.')
