import pymysql
from pymysql.cursors import DictCursor


class Mysql:
    #获取连接
    def __init__(self,
                 host="",
                 user="",
                 password="",
                 port=3306,
                 charset="utf8",
                 database="",
                 cursorclass=DictCursor):

        self.cnn = pymysql.connect(host=host,
                              user= user,
                              password=password,
                              port=port,
                              charset=charset,
                              database=database,
                              cursorclass=cursorclass)

    def query(self,sql, query_one = True):
        # 获取游标
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql)
        self.cnn.commit()
        if query_one:
            db_data = self.cursor.fetchone()
            self.cursor.close()
            return db_data
        db_data = self.cursor.fetchall()
        self.cursor.close()
        return db_data

    def query_close(self):
        self.cnn.close()


if __name__ == '__main__':
    do_mysql = Mysql(host = "8.129.91.152",
                    user = "future",
                    password = "123456",
                    port = 3306,
                    charset = "utf8",
                    database = "futureloan")
    data = do_mysql.query("select * from member LIMIT 10;", query_one=False)
    do_mysql.query_close()
    print(data)
