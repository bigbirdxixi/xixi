#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print("type integers:")

total = 0
count = 0

while True:
    try:
        line = input("PLEASE")
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count=",count,"total =",total,"mean =",total/count)
