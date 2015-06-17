#!/usr/bin/sh
# analysis 
# 根据输入的用户ID给出分析得到的结论

PEOPLE_ID=$1

sql_str="select title from people_like where people_id='${PEOPLE_ID}'"
echo $sql_str
sql_str1="select people_like.title from people_contacts inner join people_like on people_contacts.people_id=people_like.people_id where people_contacts.people_id='${PEOPLE_ID}' order by rand() limit 1000;"
mysql -uroot -p159753 -e "${sql_str}" -Dgraduation_project > $PEOPLE_ID
mysql -uroot -p159753 -e "${sql_str1}" -Dgraduation_project >> $PEOPLE_ID
python testJieba.py $PEOPLE_ID
#rm $PEOPLE_ID
