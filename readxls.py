#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd


xls_file = '/home/thomas/Documents/xls2pgsql/fepstest.xls'

wb = xlrd.open_workbook(xls_file)

ws = wb.sheet_by_name('Feuil1')

nb_rows = ws.nrows #3
nb_cols = ws.ncols #4

l = 1
c = 0

while l < nb_rows:
	while c < nb_cols:
		if c == 0:
			date = xlrd.xldate_as_tuple(int(ws.row(l)[c]), 1)
			print date
		else:
			print ws.row(l)[c]
		c += 1
	c = 0
	l += 1




# print (wb.sheet_names())
