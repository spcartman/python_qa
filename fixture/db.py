import pymysql


class DBFixture:

    def __init__(self, host, db_name, user, password):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=db_name, user=user, password=password)

    def destroy(self):
        self.connection.close()
