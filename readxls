#!/usr/bin/env/python27

import xlrd


wb = xlrd.open_workbook('D:/python/excel/test.xls')

ws = wb.sheet_by_name('Feuil1')


nb_rows = ws.nrows  # 2

i = 0

while i < nb_rows:
	row = ws.row(i)
	i += 1
	print row



# print (wb.sheet_names())
