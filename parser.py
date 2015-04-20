#!-*- coding:utf8 -*-
import urllib2
import json
import lxml
import re

def RelationParser(content):
    pass

def contactParser(content):
    # 主要作用就是解析用户关注/被关注人的信息
    cp = re.compile('<dd><a href="([^"]+)">([^<]+)</a></dd>')
    contactList = cp.findall(content)
    peopleList = [ item[1] for item in contactList ]
    return peopleList
    

    
