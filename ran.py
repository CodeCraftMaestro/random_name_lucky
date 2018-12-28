# -*- coding: utf-8 -*-

import random
import time

name = ["AAA","BBB","CCC","DDD","EEE","FFF","GGG","HHH","III","JJJ","KKK","LLL","MMM","NNN","OOO","PPP",
        "QQQ","RRR","SSS","TTT","UUU","VVV","WWW","XXX","YYY","ZZZ"]

for i in range(10):
    print("นับถอยหลัง: ",10-i)
    time.sleep(1)

congrat = random.choice(name)

name.remove(congrat)

congrat2 = random.choice(name)

print("---------------------------------")
print("ขอแสดงความยินดีกับ \nคุณ. %s \nคุณ. %s" %(congrat,congrat2))
print("---------------------------------")
