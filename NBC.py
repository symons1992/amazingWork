#-*- coding:utf8 -*- 
'''
	@author: sysmon1992
	@desc: Native Bayes Classify
'''

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



