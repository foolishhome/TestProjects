import pymysql

class JTPDBMysql:
    HOST = 'localhost'
    PORT = 3306
    DB = 'mysql_test'
    USER = 'mysql_test'
    PASSWORD = 'mysql_test'

    _conn = None
    _cursor = None

    def __init__(self, host=HOST, port=PORT, db=DB, user=USER, password=PASSWORD):
        self._password = password
        self._user = user
        self._db = db
        self._host = host
        self._port = port

    def connect(self):
        self._conn = pymysql.connect(host=self._host, port=self._port, db=self._db, user=self._user, password=self._password)
        if (self._conn):
            self._cursor = self._conn.cursor(pymysql.cursors.DictCursor)
            if (self._cursor):
                return True
        return False

    def close(self):
        if (self._cursor):
            self._cursor.close()
            self._cursor = None
        if (self._conn):
            self._conn.close()
            self._conn = None
