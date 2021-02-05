#!/usr/bin/python3.6

import time
import os

for x in range(5000):
    print("x is- ",x)
    time.sleep(3)
for y in range(10):
    print("y is-",y)
        
    os.system("s3iamcli listaccounts --ldapuser sgiamadmin --ldappasswd ldapadmin")
    os.system("s3iamcli ListAccessKeys --access_key AKIADAI_ycGERvuxTHY6ADKJlA --secret_key qzqcHpVNHWhxfQJ4gv0RxOESUnH+1B4EfgLj78jd")
    os.system("s3iamcli ListUsers --access_key AKIADAI_ycGERvuxTHY6ADKJlA --secret_key qzqcHpVNHWhxfQJ4gv0RxOESUnH+1B4EfgLj78jd")
