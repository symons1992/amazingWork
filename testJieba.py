#!-*- coding:utf8 -*-

import sys
import jieba
import jieba.posseg as pseg
import jieba.analyse


if __name__ == '__main__':
	FILE = sys.argv[1]

	Dic = {}

	need_not_show = [ u'的', u'了', u'你', u'我', u'是', u'都', u'在', u'来',u'去',u'和']

	r = open(FILE,'r')
	for line in r:
		LIST = pseg.cut(line )
		for i in LIST:
			if i.flag != 'n':
				continue
			if i.word in need_not_show:
				continue
			if Dic.get(i.word):
				Dic[i.word] = Dic[i.word] + 1
			else:
				Dic[i.word] = 1
	r.close()
	print '关键词'

	Dic = sorted(Dic.items(), key=lambda Dic:Dic[1], reverse=True)

	cnt = 0 
	for i in Dic:
		print i[0]
		cnt = cnt + 1
		if cnt == 10:
			break

	
	'''


	Dic = {}
	r = open(FILE,'r').read()
	LIST = jieba.analyse.extract_tags(r)
	for i in LIST:
		print i
	'''



