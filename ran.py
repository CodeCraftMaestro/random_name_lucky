# -*- coding: utf-8 -*-

import random
import time

name = ["Nutchanun Teppo","Moui Small","Phattanun Yeohsakul","พนารัตน์ รุ่งเรือง","Jintana Phiubang",
        "อมรรัตน์ สีม่วง","วรรณา กาญจนโรจน์","Aun Puncharat","Wanvisa'a Kongprasert ","ญิ๋งนา ญิ๋งนา","VWan Moneygold"]

for i in range(10):
    print("นับถอยหลัง: ",10-i)
    time.sleep(1)

congrat = random.choice(name)

name.remove(congrat)

congrat2 = random.choice(name)

print("---------------------------------")
print("ขอแสดงความยินดีกับ \nคุณ. %s \nคุณ. %s" %(congrat,congrat2))
print("---------------------------------")
