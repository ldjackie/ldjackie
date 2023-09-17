#!/usr/bin/env Python3
year = input('请输入年份：')
year = int(year)
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('%s是闰年' %year)
else:
    print('%s不是闰年' %year)