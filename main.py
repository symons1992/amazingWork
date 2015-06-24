#-*- coing:utf8 -*-
'''
	@author: symons1992
	@desc: the interface 
'''

import sys
from connectDB import Con
from tool import if_exist_user, get_user_like, init_dic, map_tag
from crawlData import Crawl

if __name__ == '__main__':
	user_id = sys.argv[1]
	# if the user_name in database then use it or start crawl program
	res = if_exist_user(user_id)
	if res:
		print 'has the data'
		print res
	else:
		print 'no data\n'\
			  'need to crawl the data'
	Crawl(user_id)
	
	userLikeList = get_user_like(user_id)
	userLikeDict, total = init_dic(userLikeList)
	print 'total=%s'%total
	res = map_tag(userLikeDict, total)
	print type(res)
	for i in res:
		print i[0],i[1]



