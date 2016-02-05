#!/usr/bin/env python3
# -*- coding: utf-8

import csv
import xlrd

def xls2csv():

    xls_file = '/home/thomas/virtualenvs/xls2pgsql/fepstest.xls'

    wb = xlrd.open_workbook(xls_file)

    sh = wb.sheet_by_name('Feuil1')

    csv_file = open('fepstest.csv', 'wb')

    wr = csv.writer(fepstest.csv, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()
