#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import datetime


xls_file1 = '/home/thomas/Documents/xls2pgsql/fepstest.xls'
xls_file2 = 'D:\\python\\xls2pgsql\\fepstest.xls'

wb = xlrd.open_workbook(xls_file1)

ws = wb.sheet_by_name('Feuil1')

nb_rows = ws.nrows #3
nb_cols = ws.ncols #4

l = 1
c = 0

while l < nb_rows:

	while c < nb_cols:

		# Si on se trouve dans la colonne date
		if c == 0:

			# datcell : instance de classe <class 'xlrd.sheet.Cell'>
			datcell = ws.cell(l, c)

			# dateps : stocke valeur de la cellule
			dateps = ws.cell(l, c).value

			# Stockage des éléments de la date
			year, month, day, hour, minute, second = (xlrd.xldate_as_tuple(dateps, wb.datemode))

			# Formatage de la date en yyy-mm-dd hh:mm:ss
			dateps = datetime.datetime(year, month, day, hour, minute, second)

			print dateps

		else:
			print ws.row(l)[c]
		c += 1
	c = 0
	l += 1
	
