#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd


path = '/home/thomas/Documents/xls2pgsql/fepstest.xls'

wb = xlrd.open_workbook(path)

ws = wb.sheet_by_name('Feuil1')

nb_rows = ws.nrows

i = 0

while i < nb_rows:
	row = ws.row(i)
	i += 1
	print row



# print (wb.sheet_names())
