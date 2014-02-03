import sqlite3

class SqliteShell:
    def __init__(self, dosya):
        self.dosya = dosya
        self.connection = sqlite3.connect(self.dosya)
        self.cursor = self.connection.cursor()
   
    def run(self):
        girdi = ""

        while girdi != "cikis":
            try:
                girdi = raw_input("sqlite> ")
                self.cursor.execute(girdi)
                print self.cursor.fetchall()
            except Exception as e:
                print e
        
        self.cursor.close()
        self.connection.close()

shell = SqliteShell("sqlitetest.db")
shell.run()


