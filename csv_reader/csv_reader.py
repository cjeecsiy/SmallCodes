#!/usr/bin/env python

import sys
from datetime import datetime
#import mysql.connector

class CsvReader(object):
    def proc(self):

        i = 0

        #cnx = mysql.connector.connect(user='', password='', host='', database='', charset='utf8')
        #cur = cnx.cursor(bufferd=True)

        for line in open("test.csv"):
            itemlist = line[:-1].split(',')
            (aa, bb, cc, dd, ee, ff) = tuple(itemlist)
            date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

            query = 'insert into hogehoge ('\
                    'aa, bb, cc, dd, ee, ff, gg'\
	            ') values ('\
	            ' %s, %s, %s, %s, %s, %s, %s )'  % ( aa, bb, cc, dd, ee, ff, date)
            #cur.execute(query)
            print query
    
            i += 1
            if i >= 1000:
                # cur.execute(query)
                # cnx.commit()
                print i 
                i = 0 

    def __init__(self):
        self.proc()

if __name__ == '__main__':
    CsvReader()

