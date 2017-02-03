#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3




def table_is_exist(cur, table):
	sql = "SELECT COUNT(*) FROM sqlite_master where type='table' and name='" + table + "'"
	ret = cur.execute(sql)
	return ret.fetchall()[0][0] == 1

def table_drop(conn, cur, table):
	sql = "DROP TABLE IF EXISTS " + table
	cur.execute(sql)
	conn.commit()

def table_create(conn, cur, table, titles):
	sql = "CREATE TABLE " + table + " (" + titles + ")"
	print(sql)
	cur.execute(sql)
	conn.commit()



def sql_test():
	con = sqlite3.connect('C:\\test\\python_test\\mydatabase.db3')
	cur = con.cursor()

	print(table_is_exist(cur, "foo"))
	print(table_is_exist(cur, "fox"))


	if table_is_exist(cur, "foo"):
		table_drop(con, cur, "foo")

	table_create(con, cur, "foo", "id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30)")

	cur.execute('INSERT INTO foo (id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
	cur.execute('INSERT INTO foo (id, fruit, veges) VALUES(NULL, "orange", "hava")')
	cur.execute('INSERT INTO foo (id, fruit, veges) VALUES(NULL, "pig", "green")')
	con.commit()

	print(cur.lastrowid)

	cur.execute('SELECT * FROM foo')
	print(cur.fetchall())
	con.close()


if __name__ == '__main__':
	sql_test()