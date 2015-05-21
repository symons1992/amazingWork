#!-*- coding:utf8 -*-

from crawler import CrawlData
import Queue
			
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
		if temp.step == 4:
			continue
		try:
			c = CrawlData(temp.people_id)
			c.crawl_like()
			contact_people = c.crawl_contact() or []
			contact_people = contact_people + c.crawl_rev_contact()
			# 去重，去掉互相关注的用户
			contact_people = list(set(contact_people))
			for i in contact_people:
				step = Step(i, temp.step + 1)
				q.put(step)
		except :
			print 'error id ', str(temp.people_id)
			w.write('error_id: %s\n'%(temp.people_id))
	return 

if __name__ == '__main__':
	#入口
	Crawl('103271228')




