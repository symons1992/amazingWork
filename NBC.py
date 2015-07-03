#-*- coding:utf8 -*- 
'''
	@author: sysmon1992
	@desc: Native Bayes Classify
'''

import json
import sys
import jieba
import jieba.posseg as pseg
import jieba.analyse
from constants import not_show

def count_wrods(FILE):
	r = open(FILE, 'r')
	cnt = 0 
	Dic = {}
	for line in r:
		cnt += 1
		LIST = pseg.cut(line)
		for i in LIST:
			if i.flag != 'n':
				continue
			if i.word in not_show:
				continue
			if Dic.get(i.word):
				Dic[i.word] = Dic[i.word] + 1
			else:
				Dic[i.word] = 1
	
	r.close()

def load_res():
	r = open('data_res','r').read().strip()
	dic = json.loads(r)
	return dic

def NBC(x):
	dic = load_res()
	sign = ['sport', 'sign', 'travel']
	if_sport = 0
	if_sign = 0
	if_travel = 0
	if x['sport']:
		if_sport = 1
	if x['travel']:
		if_travel = 1
	if x['sign']:
		if_sign = 1

	yes_res = 1
	not_res = 1
	if if_sport :
		yes_res = dic['friend'] * dic['sport_friend']
		not_res = dic['not_friend'] * dic['sport_not_friend']
	else:
		yes_res = dic['friend'] * dic['not_sport_friend']
		not_res = dic['not_friend'] * dic['not_sport_not_friend']
	if if_travel :
		yes_res *= dic['travel_friend']
		not_res *= dic['travel_not_friend']
	else:
		yes_res *= dic['not_travel_friend']
		not_res *= dic['not_travel_not_friend']
	if if_sign:
		yes_res *= dic['sign_friend']
		not_res *= dic['travel_not_friend']
	else:
		yes_res *= dic['not_sign_friend']
		not_res *= dic['not_sign_not_friend']
	# 添加规则，如果文章树木少于10篇且不为0的话，则减权
	if x['likes_count'] < 10 and x['likes_count'] != 0:
		yes_res = yes_res - 0.05
	if yes_res < 0:
		yes_res = 0
	return yes_res, not_res


