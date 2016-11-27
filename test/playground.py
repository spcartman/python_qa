# import mysql.connector
# import pymysql
# from model.contact import Contact
#
# conn = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     conn.close()
#
# c1 = Contact(id='1', fname='First', lname='Last', address1='Lane 1')
# c2 = Contact(id='2', fname='First', lname='Last', address1='Lane 2')
#
#
# def test_equal():
#     assert c1 == c2

input_s = '    h    a h  k   k        j  l  '
output_s = ''
count = 0
for i in range(len(input_s)):
    if input_s[i] == ' ':
        count += 1
    else:
        count = 0
    if count < 2:
        output_s += input_s[i]

print('in: ' + input_s + '.')
print('out: ' + output_s + '.')
print('better: ' + ' '.join(input_s.split()) + '.')
