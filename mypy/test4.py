#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random

gc = ["这","一个","那","此"]
zt = ["猫","狗","熊","爷们儿","美女"]
dc = ["跑","跳","叫","唱歌","打呼噜"]
zy = ["懒","贪玩","漂亮","扯把子","邋遢"]

c = input("请输入句子行数：")
a = 0
while a < int(c):
    s = random.randint(1,2)
    if s == 1:
        line = random.choice(gc)
        line += random.choice(zt)
        line += random.choice(dc)
        line += random.choice(zy)
    else:
        line = random.choice(gc)
        line += random.choice(zt)
        line += random.choice(dc)
        print(line)
        a += 1
