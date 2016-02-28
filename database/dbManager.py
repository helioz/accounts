import sqlite3 as lite
import sys


dbName = "database/trial1.db"

class DbMaker(object):
    con = None
    def __init__(self,databaseName):
        con = lite.connect(databaseName)
        with con:
            cur = con.cursor()
            cur.execute("""
            create table Clients(
            ClientID integer primary key autoincrement,
            Name text not null,
            PhoneNumber char(14) unique,
            BalanceAmount int not null,
            Notes text
            )""")

            cur.execute("""
            create table services(
            ServiceId integer primary key autoincrement,
            Name text not null,
            PhoneNumber char(14) unique,
            Notes text
            )""")

            cur.execute("""
            create table Transactions(
            TransactionId integer primary key autoincrement,
            ClientId int not null,
            ServiceId int not null,
            Amount int not null,
            TransactionDate date not null,
            Notes text,
            foreign key(clientId) references clients(clientId),
            foreign key(serviceId) references services(serviceId)
            )""")

            cur.execute("""
            create table clientTransactions(
            TransactionId integer primary key autoincrement,
            ClientId int not null,
            Amount int not null,
            TransactionDate date not null,
            Notes text,
            foreign key(clientId) references services(clientId)
            )""")


class DatabaseLayer(object):
    con = None
    def __init__(self,dbName):
        self.con = lite.connect(dbName)

    def addClient(self,cname,phoneNumber,note):
        with self.con:
            cur = self.con.cursor()
            cur.execute('Insert into clients (name,phonenumber,balanceamount,notes) values("{}","{}",0,"{}")'.format(cname,phoneNumber,note))
            return cur.lastrowid

    def addService(self,cname,phoneNumber,note):
        with self.con:
            cur = self.con.cursor()
            cur.execute('Insert into services (name,phonenumber,notes) values("{}","{}","{}")'.format(cname,phoneNumber,note))
            return cur.lastrowid


    def clientCredit(self,cid,amount,notes):
        with self.con:
            cur = self.con.cursor()
            cur.execute("Update clients set balanceamount = balanceamount + {} where clientId = {}".format(amount,cid))
            cur.execute('Insert into clientTransactions (clientId,amount,transactionDate,notes) values ({},{},current_date,"{}")'.format(cid,amount,notes))


    def clientDebit(self,cid,sid,amount,notes):
        with self.con:
            cur = self.con.cursor()
            cur.execute("update clients set balanceamount = balanceamount - {} where clientId = {}".format(amount,cid))
            cur.execute("insert into transactions (clientid,serviceid,amount,transactiondate,notes) values ({},{},{},current_date,'{}')".format(cid,sid,amount,notes))

    def getAmountIn(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("select sum(BalanceAmount) from clients")
            (value,) = cur.fetchone()
            return value


    def getAllTransactions(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute('select t.transactionid,c.name,s.name,t.amount,t.transactionDate,t.notes from clients as c,services as s,transactions as t where c.clientid = t.clientid and s.serviceid = t.serviceid')
            rows = cur.fetchall()
            return rows

    def getAllTransactionsOn(self,date):
        with self.con:
            cur = self.con.cursor()
            cur.execute("select t.transactionid,c.name,s.name,t.amount,t.transactionDate,t.notes from clients as c,services as s,transactions as t where c.clientid = t.clientid and s.serviceid = t.serviceid and t.transactionDate = '{}'".format(date))
            rows = cur.fetchall()
            return rows

    def getTrasactionsOfService(self,sid):
        with self.con:
            cur = self.con.cursor()
            cur.execute("select t.transactionid,c.name,s.name,t.amount,t.transactionDate,t.notes from clients as c,services as s,transactions as t where c.clientid = t.clientid and s.serviceid = {} and t.serviceid = {}".format(sid,sid))
            rows = cur.fetchall()
            return rows

    def getTrasactionsOfClient(self,cid):
        with self.con:
            cur = self.con.cursor()
            cur.execute("select t.transactionid,c.name,s.name,t.amount,t.transactionDate,t.notes from clients as c,services as s,transactions as t where c.clientid = t.clientid and s.serviceid = t.serviceid and c.clientid = {}".format(cid))
            rows = cur.fetchall()
            return rows
    

#########Trials
#db = DatabaseLayer(dbName)
#db.clientDebit(2,1,500,"None")
#rows = db.getTrasactionsOfClient(2)
#for row in rows:
#    print row
#db.getAllTransactions()


#db.addClient("Some Du 4","+8925346","Test guy")
#db.clientCredit(3,5000,"Testing")

#db.getAmountIn()

#db.clientDebit(1,1,1000,"Transaction okay")
#db.addService("Byson","+919572711557","Random guy for trials")

#manager = DbMaker(dbName)
