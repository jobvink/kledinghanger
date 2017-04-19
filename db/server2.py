#!/usr/bin/env python

import MySQLdb


db = MySQLdb.connect("185.104.29.62", "monitor", "password", "temps")
curs=db.cursor()