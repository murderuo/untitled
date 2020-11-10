import sqlite3

class database_tool:
    # def __init__(self,*args):
    #     self._db_name=""

    # def get_dbValues(self,*args):
    #     print(len(args))
    #     if len(args)==7:
    #         self._db_name=args[0]+".db"
    #         self._tableName=args[1]
    #         self._column1=args[2]
    #         self._column2=args[3]
    #         self._column3=args[4]
    #         self._column4=args[5]
    #         self._column5=args[6]
    #         # print(args)
    #         return self.dbConnect()
    #     else:
    #         self._db_name="database.db"
    #         self._tableName="Personel"
    #         self._column1="Adi"
    #         self._column2="Soyadi"
    #         self._column3="Tc_No"
    #         self._column4="Oda_No"
    #         self._column5="Dahili"
    #         self.dbConnect()

    def dbConnect(self):
        try:
            self.db_con=sqlite3.connect(self._db_name)
            self.db_con.close()
            return True
        except:
            # print("Database\'e bağlanılamadı...")
            return False

    def dbClose(self):
        try:
            # if self.db_con:
            self.db_con.close()
            return True
        except:
            return False


    def createTable(self):
        try:
            self.db_con=sqlite3.connect(self._db_name)
        except:
            print("connection fail")

        if self.db_con:
            self.db_cursor=self.db_con.cursor()
            sql_query="CREATE TABLE "
            sql_query+=self._tableName+"(Numara INTEGER PRIMARY KEY AUTOINCREMENT,"
            sql_query+=self._column1+" VARCHAR,"
            sql_query+=self._column2+" VARCHAR,"
            sql_query+=self._column3+" INTEGER ,"
            sql_query+=self._column4+" INTEGER ,"
            sql_query+=self._column5+" INTEGER )"
            try:
                self.db_cursor.execute(sql_query)
                self.db_con.commit()
                self.db_con.close()
                return True
            except:
                # print("Tablo oluşturulamadı")
                self.db_con.close()
                return False
        else: return False

    def insertValue(self,*args):
        if len(args)!=5:
            return False
        else:
            try:
                self.db_con=sqlite3.connect(self._db_name)
            except:
                print("connection fail")

            if self.db_con:
                self.db_cursor=self.db_con.cursor()
                insert_query="INSERT INTO "
                insert_query+=self._tableName + " ( "
                insert_query+=self._column1+" , "
                insert_query+=self._column2+" , "
                insert_query+=self._column3+" , "
                insert_query+=self._column4+" , "
                insert_query+=self._column5+" ) VALUES (?,?,?,?,?)"
                try:
                    self.db_cursor.execute(insert_query,args)
                    self.db_con.commit()
                    self.db_con.close()
                    return True
                except:
                    # print("Tablo oluşturulamadı")
                    self.db_con.close()

                    return False

    def getallValues(self):
        try:
            self.db_connect()
            self.db_cursor=self.db_con.cursor()
            getvaluequery="SELECT * FROM "
            getvaluequery+=self._tableName
            self.values=self.db_cursor.execute(getvaluequery)
            self.values=self.values.fetchall()
            self.db_con.commit()
            self.db_con.close()
            return self.values
        except:
            return False

    def getselectedValue(self,entryNo):
        try:
            # v=(entryNo,)
            self.db_connect()
            self.db_cursor=self.db_con.cursor()
            selectedquery="SELECT "
            selectedquery+=self._column1+","
            selectedquery+=self._column2+","
            selectedquery+=self._column3+","
            selectedquery+=self._column4+","
            selectedquery+=self._column5+" FROM "
            selectedquery+=self._tableName+" WHERE Numara=?"
            self.value=self.db_cursor.execute(selectedquery,(entryNo,))
            self.value=self.value.fetchone()
            self.db_con.commit()
            self.db_con.close()
            return self.value
        except:
            return False

    def updateselectedValue(self,no,*args):

        try:
        # v=(no,)
            self.db_connect()
            self.db_cursor=self.db_con.cursor()
            updatequery="UPDATE "
            updatequery+=self._tableName+" SET "
            updatequery+=self._column1+"=?"+","
            updatequery+=self._column2+"=?"+","
            updatequery+=self._column3+"=?"+","
            updatequery+=self._column4+"=?"+","
            updatequery+=self._column5+"=? WHERE Numara=?"
            # selectedquery+=entryNo
            self.db_cursor.execute(updatequery,(*args,no,))
            self.db_con.commit()
            self.db_con.close()
            return True
        except:
            return False

    def deleteEntry(self,no):
        try:
            self.db_connect()
            self.db_cursor=self.db_con.cursor()
            deletevaluequery="DELETE FROM "
            deletevaluequery+=self._tableName + " WHERE Numara=?"
            self.db_cursor.execute(deletevaluequery,(no,))
            self.db_con.commit()
            self.db_con.close()
            return True
        except:
            return False




# if __name__ == '__main__':
    # dbtool=database_tool("test","personel","adi","soyadi","tc","odano","dahili")

    # status=dbtool.db_connect()
    # # print("database connect",status)
    # create_db_status=dbtool.createTable()
    # print("create db status",create_db_status)
    # insert_status=dbtool.insertValue("feyyaz","dağdeviren","112312313","asdasd","67ykghjk")
    # print("insert status",insert_status)
    # data=dbtool.getallValues() #get data
    # print(data)#print getted data
    #
    # selected=dbtool.getselectedValue("10")
    # print(selected)
    #
    # update_stat=dbtool.updateselectedValue("11","mehmet","battal","123123123","45","2")
    # print(update_stat)
    #
    # selected=dbtool.getselectedValue("11")
    # print(selected)