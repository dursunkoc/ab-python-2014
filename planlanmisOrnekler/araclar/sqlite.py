#-*- encoding: utf-8 -*-
import sqlite3


class SqliteShell:
    """
    create table kisiler (type text, ad text, soyad text, email text, tckno text, telno text, ogrencino text)
    SELECT name FROM sqlite_master WHERE type='table';
    SELECT SQLITE_VERSION();
    PRAGMA table_info(Cars);
    SELECT name FROM sqlite_master WHERE type='table'
    """

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def run(self):
        girdi = ""
        tampon = ""

        while girdi != "cikis":
            if sqlite3.complete_statement(tampon):
                try:
                    self.cursor.execute(girdi)
                    data = self.cursor.fetchall()
                    print "{0}".format(data)
                except Exception as e:
                    print e
                finally:
                    tampon = ""
            elif tampon != "":
                girdi = raw_input("... ")
                tampon += girdi
            else:
                girdi = raw_input("sqlite> ")
                tampon += girdi

        self.connection.close()

if __name__ == "__main__":
    shell = SqliteShell("/home/serhat/test2.db")
    shell.run()
