#-*- coding:utf8 -*-

from parser import Parser
from models import People
import urllib2
import re
from lxml import html
import time

class CrawlData:
	def __init__(self, id):
		self.id = id
	# 抓取用户喜欢页信息，可翻页
	def crawl_like(self):
		base_url = "http://www.douban.com/people/people_id/likes/"
		url = base_url.replace("people_id",self.id)
		while 1:
			#睡眠5s钟，防止被封
			time.sleep(5)
			request = urllib2.Request(url)
			request.add_header('cookie', 'bid="HyPHE9q0u6E"; ll="108288"; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1429524161%2C%22http%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E5%2590%258E%25E5%258F%25B0%25E5%25BC%2580%25E5%258F%2591%2520c%252B%252B%26rsv_pq%3Db4233f3500010802%26rsv_t%3D520cQFmLzqO8GXz%252F%252FWnDaxdx32JcIgtxAQHLb4SYiDT5zu9esPJygw%252BK3kw%26rsv_enter%3D1%26rsv_sug3%3D19%26rsv_sug1%3D16%26rsv_sug2%3D0%26inputT%3D5583%26rsv_sug4%3D5584%22%5D; ps=y; ue="234039148@qq.com"; __utmt=1; dbcl2="40985129:16vGtrMq1kA"; ck="YqA_"; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=faeed9cc848812fb.1427793954.16.1429527430.1429512088.; _pk_ses.100001.8cb4=*; __utma=30149280.1757349605.1427793954.1429524129.1429526516.23; __utmb=30149280.27.9.1429527430295; __utmc=30149280; __utmz=30149280.1429526516.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E9%AA%8C%E8%AF%81%E7%A0%81%20%E6%8A%93%E5%8F%96; __utmv=30149280.4098; ap=1')

			raw_content = urllib2.urlopen(request).read()
			# 解析入库
			Parser.parseLike(self.id, raw_content)

			#若可以翻页
			if 'rel="next"' in raw_content:
				page = html.fromstring(raw_content)
				url = page.find_class('next')[0].xpath('./link')[0].get('href')
			else:
				break
	
	# 抓取用户关注信息
	def crawl_contact(self):
		base_url = "http://www.douban.com/people/people_id/contacts/"
		url = base_url.replace("people_id",self.id)
		time.sleep(5)
		request = urllib2.Request(url)
		request.add_header('cookie', 'bid="HyPHE9q0u6E"; ll="108288"; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1429524161%2C%22http%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E5%2590%258E%25E5%258F%25B0%25E5%25BC%2580%25E5%258F%2591%2520c%252B%252B%26rsv_pq%3Db4233f3500010802%26rsv_t%3D520cQFmLzqO8GXz%252F%252FWnDaxdx32JcIgtxAQHLb4SYiDT5zu9esPJygw%252BK3kw%26rsv_enter%3D1%26rsv_sug3%3D19%26rsv_sug1%3D16%26rsv_sug2%3D0%26inputT%3D5583%26rsv_sug4%3D5584%22%5D; ps=y; ue="234039148@qq.com"; __utmt=1; dbcl2="40985129:16vGtrMq1kA"; ck="YqA_"; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=faeed9cc848812fb.1427793954.16.1429527430.1429512088.; _pk_ses.100001.8cb4=*; __utma=30149280.1757349605.1427793954.1429524129.1429526516.23; __utmb=30149280.27.9.1429527430295; __utmc=30149280; __utmz=30149280.1429526516.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E9%AA%8C%E8%AF%81%E7%A0%81%20%E6%8A%93%E5%8F%96; __utmv=30149280.4098; ap=1')

		raw_content = urllib2.urlopen(request).read()
		# 解析入库
		Parser.parseContact(self.id, raw_content)

		return 


	# 抓取用户被关注信息
	def crawl_rev_contact(self):
		base_url = "http://www.douban.com/people/people_id/rev_contacts/"
		url = base_url.replace("people_id",self.id)
		time.sleep(5)
		request = urllib2.Request(url)
		request.add_header('cookie', 'bid="HyPHE9q0u6E"; ll="108288"; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1429524161%2C%22http%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E5%2590%258E%25E5%258F%25B0%25E5%25BC%2580%25E5%258F%2591%2520c%252B%252B%26rsv_pq%3Db4233f3500010802%26rsv_t%3D520cQFmLzqO8GXz%252F%252FWnDaxdx32JcIgtxAQHLb4SYiDT5zu9esPJygw%252BK3kw%26rsv_enter%3D1%26rsv_sug3%3D19%26rsv_sug1%3D16%26rsv_sug2%3D0%26inputT%3D5583%26rsv_sug4%3D5584%22%5D; ps=y; ue="234039148@qq.com"; __utmt=1; dbcl2="40985129:16vGtrMq1kA"; ck="YqA_"; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=faeed9cc848812fb.1427793954.16.1429527430.1429512088.; _pk_ses.100001.8cb4=*; __utma=30149280.1757349605.1427793954.1429524129.1429526516.23; __utmb=30149280.27.9.1429527430295; __utmc=30149280; __utmz=30149280.1429526516.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E9%AA%8C%E8%AF%81%E7%A0%81%20%E6%8A%93%E5%8F%96; __utmv=30149280.4098; ap=1')

		raw_content = urllib2.urlopen(request).read()
		# 解析入库
		Parser.parseRevContact(self.id, raw_content)

		return 




if __name__ == '__main__':
	'''
		@eg: c = CrawlData('')
			 c.crawl_like()
	'''
	#以后测试要保留这个接口，其他隐私信息会写在test.py  <----是不会上传到github上的。

	c = CrawlData('103271228')
	#c.crawl_like()
	c.crawl_contact()
	c.crawl_rev_contact()


