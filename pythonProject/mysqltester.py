from jtp.jtp_mysql import JTPDBMysql
import unittest


def check_it():
    db = JTPDBMysql(host='192.168.0.105', db='testdb', user='root', password='Fuckyou1!') # JTPDBMysql.HOST, JTPDBMysql.PORT, JTPDBMysql.DB, JTPDBMysql.USER, JTPDBMysql.PASSWORD

    try:
        if (db.connect()):
            db._cursor.execute("select * from testdb.fuckdb limit 10")
            data = db._cursor.fetchone()
            print("-- 当前数量: %s " % data)
            db.close()
            return True
    except Exception as error:
        print(error)
    return False

class TestMysql(unittest.TestCase):
    def test_connection(self):
        print(f'tester, {self}')
        self.assertEqual(True, check_it())  # add assertion here
    def test_dbandtables(self):
        pass
    def test_form(self):
        pass

if __name__ == '__main__':
    unittest.main()
