import pymysql.cursors;

class DB_Users:
    def __init__(self, connection):
        self._connection = connection;
        self._createTable();

    def _setData(self, serverID, accountID, data, dataType):
        try:
            with self._connection.cursor() as cursor:
                sql = "update `Users` set `{0}` = %s where `ServerID` = %s and `AccountID` = %s".format(dataType);
                print(sql);
                cursor.execute(sql, (data, serverID, accountID));
            self._connection.commit();
        except:
            return;

    def _getData(self, serverID, accountID, dataType):
        try:
            with self._connection.cursor() as cursor:
                sql = "select * from `Users` where `ServerID` = %s and `AccountID` = %s";
                cursor.execute(sql, (serverID, accountID));
                result = cursor.fetchone()[dataType];
        finally:
            return result;

    def setNIM(self, serverID, accountID, NIM):
        try:
            with self._connection.cursor() as cursor:
                sql = "insert into `Users` (`ServerID`, `AccountID`, `NIM`) values (%s, %s, %s)";
                cursor.execute(sql, (serverID, accountID, NIM));
            self._connection.commit();
        except:
            self._setData(serverID, accountID, NIM, "NIM");
    def getNIM(self, serverID, accountID):
        return self._getData(serverID, accountID, "NIM");

    def setPhoneNumber(self, serverID, accountID, phoneNumber):
        self._setData(serverID, accountID, phoneNumber, "PhoneNumber");
    def getPhoneNumber(self, serverID, accountID):
        return self._getData(serverID, accountID, "PhoneNumber");

    def setBankAccount(self, serverID, accountID, bankAccount):
        self._setData(serverID, accountID, bankAccount, "BankAccount");
    def getBankAccount(self, serverID, accountID):
        return self._getData(serverID, accountID, "BankAccount");

    def _createTable(self):
        # 2019-0417
        try:
            with self._connection.cursor() as cursor:
                sql = """
                    CREATE TABLE `Users`(
                        `ServerID` varchar(25) NOT NULL,
                        `AccountID` varchar(25) NOT NULL,
                        `NIM` varchar(10) NOT NULL,
                        `FullName` varchar(100) DEFAULT NULL,
                        `BankAccount` varchar(100) DEFAULT NULL,
                        `PhoneNumber` varchar(20) DEFAULT NULL
                    ) DEFAULT CHARSET=latin1;
                """;
                cursor.execute(sql);
        except:
            pass;
        finally:
            self._connection.commit();

        # 2019-0417
        try:
            with self._connection.cursor() as cursor:
                sql = """
                    ALTER TABLE `Users` ADD PRIMARY KEY (`ServerID`,`AccountID`), ADD UNIQUE KEY `NIM` (`NIM`);
                """;
                cursor.execute(sql);
        except:
            pass;
        finally:
            self._connection.commit();
