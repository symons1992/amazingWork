#-*- coding:utf8 -*-
import sys
from connectDB import Con
from tool import if_exist_user, get_user_like, init_dic, map_tag
from crawlData import Crawl
import json

def train():
	outfile = 'trainng_res'
	w = open(outfile,'w')
	userlist = open('training_list','r')
	cnt = 0
	for user_id in userlist:
		cnt += 1
		user_id = user_id.strip()
		res = if_exist_user(user_id)
		'''
		if res:
			print 'yes'
		else:
			Crawl(user_id)
			print 'crawl success'
		'''
		userLikeList = get_user_like(user_id)
		userLikeDict, total = init_dic(userLikeList)
		res = map_tag(userLikeDict, total)
		x = { 'user_id': user_id,
			  'sport': 0,
			  'sign': 0,
			  'travel': 0,
			  'friend': 1
			  }
		if cnt >= 10:
			x['friend'] = 0
		for i in res:
			print i[0],i[1]
			if i[0] == u'星座':
				if i[1] >= 5:
					x['sign'] = 1
			if i[0] == u'旅游':
				if i[1] >= 5:
					x['travel'] = 1
			if i[0] == u'运动':
				if i[1] >= 5:
					x['sport'] = 1

		w.write(json.dumps(x)+'\n')
		print json.dumps(x)

def count():
	r = open('trainng_res','r')
	w = open('data_res', 'w')
	total = 15
	sport_friend = 0
	sport_not_friend = 0
	sign_friend = 0
	sign_not_friend = 0
	travel_friend = 0
	travel_not_friend = 0
	friend = 0
	not_friend = 0

	for line in r:
		dic = json.loads(line.strip())
		if dic['travel'] == 1 and dic['friend'] == 1:
			travel_friend += 1
		if dic['travel'] == 1 and dic['friend'] == 0:
			travel_not_friend += 1
		if dic['sport'] == 1 and dic['friend'] == 1:
			sport_friend += 1
		if dic['sport'] == 1 and dic['friend'] == 0:
			sport_not_friend += 1
		if dic['sign'] == 1 and dic['friend'] == 1:
			sign_friend += 1
		if dic['sign'] == 1 and dic['friend'] == 0:
			sign_not_friend += 1
		if dic['friend'] == 1:
			friend += 1
		if dic['friend'] == 0:
			not_friend += 1
	dic = {
			'travel_friend': travel_friend*1.0/friend,
			'not_travel_friend': 1 - travel_friend*1.0/friend,
			'travel_not_friend': travel_not_friend*1.0/not_friend,
			'not_travel_not_friend': 1 - travel_not_friend*1.0/not_friend,
			'sport_friend': sport_friend*1.0/friend,
			'not_sport_friend': 1 - sport_friend*1.0/friend,
			'sport_not_friend': sport_not_friend*1.0/not_friend,
			'not_sport_not_friend': 1 - sport_not_friend*1.0/not_friend,
			'sign_friend': sign_friend*1.0/friend,
			'not_sign_friend': 1 - sign_friend*1.0/friend,
			'sign_not_friend': sign_not_friend*1.0/not_friend,
			'not_sign_not_friend': 1 - sign_not_friend*1.0/not_friend,
			'friend': friend*1.0/total,
			'not_friend': not_friend*1.0/total
			}
	w.write(json.dumps(dic)+'\n')

if __name__ == '__main__':
	train()
	count()
