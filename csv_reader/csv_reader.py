#!/usr/bin/env python

import sys
from datetime import datetime
import mysql.connector

class CsvLoader(object):

    def proc(self):
        try:
            i = 0
            config = self.__get_config()
            cnx = mysql.connector.connect(**config)
            cur = cnx.cursor(buffered=True)
            for line in open("test.csv"):
                itemlist = line[:-1].split(',')
                (aa, bb, cc, dd, ee, ff) = tuple(itemlist)
                date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

                query = (
                        'insert into hogehoge ('
                        'aa, bb, cc, dd, ee, ff, gg'
                        ') values ('
                        ' \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\'  )' 
                    ) % ( aa, bb, cc, dd, ee, ff, date)
                print query
                cur.execute(query)
        
                i += 1
                if i >= 1000:
                    cnx.commit()
                    print i 
                    i = 0 
        finally:
            cnx.commit()
            cnx.close()


    def __get_config(self):
        return {
            "database": "mysql_test",
            "host": "localhost",
            "user": "root",
            "password": "",
            "port": "3306", 
            "charset": "utf8"
        }

    def __init__(self):
        self.proc()

if __name__ == '__main__':
    CsvLoader()

