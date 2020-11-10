import sqlite3

class database_tool:

    def db_connect(self,dbname="database"):
        self.db_name=dbname+".db"
        try:
            self.db_con=sqlite3.connect(self.db_name)
            return True
        except:
            # print("Database\'e bağlanılamadı...")
            return False

    def createTable(self,*args):
        """first arg, tablename, other args are column name. i want to create one table and 5 column couse
        of this args must have to 6 argument"""
        if len(args)!=6: raise NameError("arguments must be 6 ")
        if self.db_con:
            self.db_cursor=self.db_con.cursor()
            sql_query="CREATE TABLE "
            sql_query+=args[0]+"(Numara INTEGER PRIMARY KEY AUTOINCREMENT,"
            sql_query+=args[1]+" VARCHAR,"
            sql_query+=args[2]+" VARCHAR,"
            sql_query+=args[3]+" INTEGER ,"
            sql_query+=args[4]+" INTEGER ,"
            sql_query+=args[5]+" INTEGER )"
            try:
                self.db_cursor.execute(sql_query)
                self.db_con.commit()
                self.db_con.close()
                return True
            except:
                # print("Tablo oluşturulamadı")
                return False

dbtool=database_tool()
status=dbtool.db_connect("test")
print("database connect",status)
table_status=dbtool.createTable('test_table', 'column1', 'column2', "column3","column4")

print("table status",table_status)









