#!/bin/sh

mysqldump -uroot -p159753 --routines --default-character-set=utf8 --no-data --databases graduation_project > graduation_project.sql
