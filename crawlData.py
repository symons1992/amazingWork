#-*- coding:utf8 -*-

from crawler import CrawlData
import Queue
from tool import if_exist_user
			
class Step:
	def __init__(self, people_id, step):
		self.people_id = people_id
		self.step = step

def Crawl(people_id):
	w = open('error People_id','a')
	q = Queue.Queue(maxsize = 100000)
	oneStep = Step(people_id, 1)
	q.put(oneStep)
	while not q.empty():
		temp = q.get()
		#if temp.step == 4:
		if temp.step == 3:
			continue
		try:
			c = CrawlData(temp.people_id)
			# 如果这个人的数据已经存在了那么就不用去抓他的数据了
			if not if_exist_user(temp.people_id):
				c.crawl_like()
			contact_people = []
			#contact_people = c.crawl_contact() or []
			#print 'contact_people: ',contact_people
			#这里取消了关注他的用户，然后把纬度降低到2维
			#contact_people = contact_people + c.crawl_rev_contact()
			# 去重，去掉互相关注的用户
			contact_people = list(set(contact_people))
			for i in contact_people:
				step = Step(i, temp.step + 1)
				q.put(step)
		except Exception,ex:
			print Exception,ex
			print 'error id ', str(temp.people_id)
			w.write('error_id: %s\n'%(temp.people_id))
	return 

# for test def
if __name__ == '__main__':
	#入口
	Crawl('mrcrow')

