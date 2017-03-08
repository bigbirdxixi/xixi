#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print("type integers:")

total = 0
count = 0
sq =[]

while True:
    try:
        line = input("enter a number or Enter to finish:")
        if line:
            number = int(line)
            total += number
            count += 1
            sq.append(number)
        else:
            break
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print(sq)
    print("count=",count,"total =",total,"minimum=",min(sq),"max=",max(sq),"mean =",total/count)
