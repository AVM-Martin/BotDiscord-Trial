import pymysql.cursors;
import cogs.utils.DB_Users as Users;

class MyDatabase:
    def __init__(self, host, user, password, db, charset="utf8mb4"):
        self._connection = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset, cursorclass=pymysql.cursors.DictCursor);
        self.Users = Users.DB_Users(self._connection);
