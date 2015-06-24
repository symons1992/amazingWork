#-*- coding:utf8 -*-
import MySQLdb

'''
	@author: symons1992
	@date:	 20150504
	@aim:    连接数据库，一系列操作
'''
#TODO : 添加读取配置文件工具，隐藏配置文件信息
class Con:
	def __init__(self):
		self.conn = MySQLdb.connect(host='localhost', user='root', passwd='159753', port=3306, charset='utf8')
		self.cur  = self.conn.cursor()
		self.conn.select_db('graduation_project')
	
	def insert_people_like(self, values):
		sql_str = "replace into people_like(people_id, title, item_type, item_url) values(%s,%s,%s,%s)"
		self.cur.execute(sql_str, values)
		self.conn.commit()
	
	def insert_people_contact(self, values):
		sql_str = "replace into people_contacts(people_id, contact_id) values(%s,%s)"
		self.cur.execute(sql_str, values)
		self.conn.commit()
	
	def query(self, sql_str):
		res = self.cur.execute(sql_str)
		return self.cur.fetchall()

	def close(self):
		self.cur.close()
		self.conn.close()


if __name__ == '__main__':
	c = Con()
	c.query('select count(*) from people_like where people_id="haha";')
	c.close()



