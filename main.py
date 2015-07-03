#-*- coding:utf8 -*-
'''
	@author: symons1992
	@desc: the interface 
'''

import json
import sys
from connectDB import Con
from tool import if_exist_user, get_user_like, init_dic, map_tag
from crawlData import Crawl
from NBC import NBC

if __name__ == '__main__':
	user_id = sys.argv[1]
	# if the user_name in database then use it or start crawl program
	res = if_exist_user(user_id)
	likes_count = 0
	if res:
		print 'has the data'
		likes_count = res
	else:
		print 'no data\n'\
			  'need to crawl the data'
		Crawl(user_id)
		print 'crawl data finish'
		if not if_exist_user(user_id):
			print 'maybe the user doesnot like to show his data'
	
	userLikeList = get_user_like(user_id)
	userLikeDict, total = init_dic(userLikeList)
	res = map_tag(userLikeDict, total)
	x = { 'user_id': user_id,
		  'sport': 0,
		  'sign': 0,
		  'travel': 0,
		  'likes_count': likes_count
		  }
	for i in res:
		if i[0] == u'星座':
			if i[1] >= 5:
				x[u'sign'] = 1
		if i[0] == u'旅游':
			if i[1] >= 5:
				x[u'travel'] = 1
		if i[0] == u'运动':
			if i[1] >= 5:
				x[u'sport'] = 1
	yes, no = NBC(x)
	print 'maybe: %s'%yes
	print 'maybe not: %s'%no
	if yes > no :
		print 'they maybe become friend'
	else:
		print 'they maybe canot become friend'


