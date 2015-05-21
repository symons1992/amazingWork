#!/usr/bin/sh

PEOPLE_ID=$1

#mysql -uroot -p159753 -e "select title from people_like where people_id='yujjme';" -Dgraduation_project > testText3
sql_str="select title from people_like where people_id='${PEOPLE_ID}'"
echo $sql_str
mysql -uroot -p159753 -e "${sql_str}" -Dgraduation_project > $PEOPLE_ID
python testJieba.py $PEOPLE_ID
rm $PEOPLE_ID
