#!/usr/bin/env python3

from __future__ import print_function

import sys
import MySQLdb
import time

### change me ###
MYSQL_HOST = 'localhost'
MYSQL_USER = 'kippo'
MYSQL_PASS = 'changeme123'
MYSQL_DB = 'kippo'
### stop changing settings ###

try:
    conn = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
except:
    print('couldnt connect to database, exiting')
    exit(-1)

start_tm = time.strftime("%Y-%m-%d", time.localtime(time.time() - (86400 * 7)))

cursor = conn.cursor()
cursor.execute("SELECT DISTINCT ip FROM sessions WHERE starttime > %(start_tm)s", {
    'start_tm': start_tm
})

out_file = open(sys.argv[1], 'w')
out_file.write('# Automatically generated file.  Do not edit!\n')
out_file.write(':1:Testing\n127.0.0.2\n')

out_file.write(':2:SSH scanning was detected from this host\n')
for i in cursor.fetchall():
    out_file.write(i[0] + '\n')

out_file.close()
