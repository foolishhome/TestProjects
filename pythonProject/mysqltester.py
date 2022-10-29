from jtp_mysql import JTPDBMysql
import unittest

def check_it():
    db = JTPDBMysql() //JTPDBMysql.HOST, JTPDBMysql.PORT, JTPDBMysql.DB, JTPDBMysql.USER, JTPDBMysql.PASSWORD

    if (db.connect()):
        db._cursor.execute("select count(id) as total from Product")
        data = db._cursor.fetchone()
        print("-- 当前数量: %d " % data['total'])
        db.close()

class TestMysql(unittest.TestCase):
    def test_connection(self):
        print(f'tester, {self}')
        check_it()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
