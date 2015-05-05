#-*- coding:utf8 -*-
import urllib2
import json
from lxml import html
import lxml
import re
from connectDB import Con

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Parser:
	#解析用户喜欢这个页面
	@classmethod
	def parseLike(cls, people_id, content):
		page = html.fromstring(content)
		titleSet = page.find_class('title')
		con = Con()
		for title_item in titleSet:
			title = title_item.xpath('./a/text()[1]')[0]
			url = title_item.xpath('./a')[0].get('href')
			Type = ''
			if 'widget' in url:
				Type = 'photo_note'
			elif 'photo' in url:
				Type = 'photo'
			elif 'note' in url:
				Type = 'note'
			print title
			con.insert_people_like((people_id, title.encode('utf8'), Type, url))
		con.close()

	#解析用户关注信息
	@classmethod
	def parseContact(cls, people_id, content):
		peopleIdPattern = re.compile('people/([\w\-_\d]+)/')
		page = html.fromstring(content)
		peoples = page.find_class('obu')
		con = Con()
		for people in peoples:
			url = people.xpath('./dd/a')[0].get('href')
			contact_id = peopleIdPattern.findall(url)[0]
			print contact_id
			con.insert_people_contact((people_id,contact_id))
		con.close()

	#解析用户被关注信息
	@classmethod
	def parseRevContact(cls, people_id, content):
		peopleIdPattern = re.compile('people/([\w\-_\d]+)/')
		page = html.fromstring(content)
		peoples = page.find_class('obu')
		con = Con()
		for people in peoples:
			url = people.xpath('./dd/a')[0].get('href')
			rev_contact_id = peopleIdPattern.findall(url)[0]
			print rev_contact_id
			#做一个reverse操作，因为该函数解析的是被xxx关注
			con.insert_people_contact((rev_contact_id,people_id))
		con.close()


