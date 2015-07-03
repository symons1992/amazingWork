#-*- coding:utf8 -*-
'''
	@author: sysmon1992
	@desc: the tool
'''

import sys
from connectDB import Con
import jieba
jieba.load_userdict("mydict.txt")
import jieba.posseg as pseg
import jieba.analyse
from constants import not_show as need_not_show
from constants import tag

def if_exist_user(user_name):
	# query the data num from people_like
	C = Con()
	sql_str = 'select count(*) from people_like where people_id="PEOPLE_ID";'
	sql_str = sql_str.replace('PEOPLE_ID',user_name)
	res = C.query(sql_str)
	C.close()
	return res[0][0]

def get_user_like(user_name):
	C = Con()
	sql_str = 'select title from people_like where people_id="PEOPLE_ID";'
	# query the user contact users and will make the result more useful
	sql_str1 = 'select people_like.title from people_contacts inner join people_like on people_contacts.people_id=people_like.people_id where people_contacts.people_id="PEOPLE_ID" order by rand() limit 2000;'
	sql_str = sql_str.replace('PEOPLE_ID', user_name)
	sql_str1 = sql_str1.replace('PEOPLE_ID', user_name)
	res = C.query(sql_str)
	res += C.query(sql_str1)
	C.close()
	res = [ i[0] for i in res ]
	return res

def init_dic(people_like_list):
	Dic = {}
	for line in people_like_list:
		items = pseg.cut(line)
		for item in items:
			if item.flag != 'n' or item.word in need_not_show or len(item.word) < 2:
				continue
			if Dic.get(item.word):
				Dic[item.word] += 1
			else:
				Dic[item.word] = 1
	Dic = sorted(Dic.items(), key=lambda Dic:Dic[1], reverse=True)
	res = []
	total = 0
	for i in Dic:
		# total 表示一共有多少个单词
		total += i[1]
		res.append((i[0],i[1]))
	return res, total

def map_tag(userLikeDict, total):
	# 拉普拉斯平滑
	res = { k:1 for k,v in tag.items() } 
	for i in userLikeDict:
		for j in tag.keys():
			if i[0] in tag[j]:
				res[j] += i[1]
	for k, v in res.items():
		if total == 0:
			v = 0
		else:
			v = v*1.0/total * 100
	res = sorted(res.items(), key=lambda key:key[1], reverse=True)

	return res[:10]

if __name__ == '__main__':
	k = map_tag([],0)
	for i,j in k.items():
		print i,j


