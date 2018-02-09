#!/usr/bin/python

import csv
import MySQLdb
import pandas as pd
import sqlalchemy
import numpy as np

def print_row(data):
    for row in data:
        print len(row),row

if __name__ == '__main__':
    # path = '/Users/bill/PycharmProjects/BeauSoupTest/'
    path = '/local/bill_test/'
    df = pd.read_csv(path + 'ticker_cik.csv')
    # print(df.columns)
    # print type(df['TRANDATE'][1])
    # df['cshoq'] = df.groupby(['tic'])['cshoq'].transform(lambda grp: grp.fillna(method='ffill'))
    # print df.iloc[1]
    # df['cshoq'] = df['cshoq']*1000000
    df = df.astype(object).where(pd.notnull(df), None)
    # df.to_sql
    A = df.values.tolist()
    # print len(A)
    # print_row(A[:5])
    db = MySQLdb.connect("localhost", "root", 'Edgar20!4', "bill")
    cursor = db.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS ticker_cik(
                        id BIGINT NOT NULL AUTO_INCREMENT,
                        tic TEXT,
                        cusip TEXT,
                        cik TEXT,
                        KEY(id)
              )'''
    cursor.execute(sql)
    query = "INSERT INTO ticker_cik(`tic`, `cusip`, `cik`)"\
                    "VALUES(%s, %s, %s)"
    # print_row()
    for row in A:
        try:
            cursor.execute(query, tuple([row[7],row[8],row[10]]))
            db.commit()
            print "db_updated"
        except MySQLdb.Error as e:
            db.rollback()
            print e
    print 'Done'


    # conn = sqlalchemy.engine.Connection()
    # cursor = db.cursor()
    # df[150:151].to_sql(con=db, name='market_cap_two2', if_exists='replace', flavor='mysql', dtype={'cshoq':
    #                                                                                                   sqlalchemy.types.DECIMAL})
    # df2[:150].to_sql(con=db, name='market_cap_two2', if_exists='append', flavor='mysql')
    # df2[151:].to_sql(con=db, name='market_cap_two2', if_exists='append', flavor='mysql')
    # df.to_sql(con=db, name='market_cap_two2', if_exists='replace', flavor='mysql', dtype={'cshoq':
    # sqlalchemy.DECIMAL})

    #
    # sql = '''CREATE TABLE IF NOT EXISTS mket_caps_0601(
    #                     id BIGINT NOT NULL AUTO_INCREMENT,
    #                     date DATE,
    #                     ticker TEXT,
    #                     price_per_share DECIMAL(19,2)
    #                     outstanding_share_1 DECIMAL(19,2)
    #                     outstanding_share_2 DECIMAL(19,2)
    #                     cik INT(11)
    #                     sic INT(11)
    #                     KEY(id)
    #           )'''
    #
    # cursor.execute(sql)
    # print 'Table created'
    # query = "INSERT INTO mket_caps_0601(`date`, `ticker`, `price_per_share`, `outstanding_share_1`," \
    #         "`outstanding_share_2`, `cik`, `sic`, " \
    #             "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

    # with open(path + 'two_mket_caps.csv', 'r') as file:
    #
    #     reader = csv.reader(file)
    #     # row_count = sum(1 for row in reader)
    #     row_count = 2493513;
    #     i = 0
    #     # print row_count
    #     for i, row in enumerate(reader):
    #         row = row[2:]
    #         print row
    #         if i >20:
    #             break
    #         else:
    #             pass
    #         # try:
    #         #     cursor.execute(query, tuple(row))
    #         #     db.commit()
    #         #     print "db_updated"
    #         # except MySQLdb.Error as e:
    #         #     db.rollback()
    #         #     print e
    #         # print 'Done'


