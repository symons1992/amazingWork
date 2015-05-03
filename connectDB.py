#-*- coding:utf8 -*-
import MySQLdb

'''
	@author: symons1992
	@date:	 20150504
	@aim:    连接数据库，一系列操作
'''
class Con:
	def __init__(self):
		self.conn = MySQLdb.connect(host='localhost', user='root', passwd='159753', port=3306, charset='utf8')
		self.cur  = self.conn.cursor()
		self.conn.select_db('graduation_project')
	
	def insert_people_like(self, values):
		sql_str = "insert into people_like(people_id, title, item_type, item_url) values(%s,%s,%s,%s)"
		self.cur.execute(sql_str,values)
		self.conn.commit()
	
	def query(self):
		pass

	def close(self):
		self.cur.close()
		self.conn.close()



