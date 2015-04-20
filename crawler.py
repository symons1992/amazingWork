#-*- coding:utf8 -*-

import urllib2
import re


def crawler(people_id):

    base_url = "http://www.douban.com/people/people_id/contacts/"
    url = base_url.replace("people_id",people_id)
    request = urllib2.Request(url)
    request.add_header('cookie', 'bid="HyPHE9q0u6E"; ll="108288"; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1429524161%2C%22http%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E5%2590%258E%25E5%258F%25B0%25E5%25BC%2580%25E5%258F%2591%2520c%252B%252B%26rsv_pq%3Db4233f3500010802%26rsv_t%3D520cQFmLzqO8GXz%252F%252FWnDaxdx32JcIgtxAQHLb4SYiDT5zu9esPJygw%252BK3kw%26rsv_enter%3D1%26rsv_sug3%3D19%26rsv_sug1%3D16%26rsv_sug2%3D0%26inputT%3D5583%26rsv_sug4%3D5584%22%5D; ps=y; ue="234039148@qq.com"; __utmt=1; dbcl2="40985129:16vGtrMq1kA"; ck="YqA_"; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=faeed9cc848812fb.1427793954.16.1429527430.1429512088.; _pk_ses.100001.8cb4=*; __utma=30149280.1757349605.1427793954.1429524129.1429526516.23; __utmb=30149280.27.9.1429527430295; __utmc=30149280; __utmz=30149280.1429526516.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E9%AA%8C%E8%AF%81%E7%A0%81%20%E6%8A%93%E5%8F%96; __utmv=30149280.4098; ap=1')

    raw_content = urllib2.urlopen(request).read()
    w = open("people_id"+str(people_id),'w')
    w.write(raw_content)
    w.close()
    #page = html.fromstring(raw_content)
    #friends = page.xpath('/body/div[3]/div/div/div/div/dl[6]/')
    #print len(friends)

if __name__ == '__main__':
    crawler('103271228')





    
    
