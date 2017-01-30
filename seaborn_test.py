#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import linecache
import re

# グラフの種類
sns.set_style("whitegrid")

args = sys.argv

#見出し行
header_line = 3
filepath = args[1]
c = int(args[2]) + header_line
e = int(args[3]) + 1

data = open(filepath, "rU")

i = 1
while i <= header_line:
  data_head = next(data) #見出し行を無視
  i += 1

data_title = ["time", "interval", "iops", "MB/s", "bytes i/o", "read pct", "resp time", "read resp", "write resp", "resp", "max", "resp stddev", "queue depth", "cpu%", "sys+u", "cpu%", "sys"]

#何行目の項目を分析するか
#x_row = 1
y_row = 2
#y2_row = 5

x = []
y = []
#y2 = []

print("start line:%i" % (c - header_line))

while c <= e:
  row = linecache.getline(filepath, c)
  row = row.replace('"', '')
  row = row.replace('/', '')
  row = row.replace(':', '')
  row = re.split(" +", row)
  #x.append(row[x_row][5:-1]) #日付を跨ぐ時順番が前後してしまう
  x.append(c)
  y.append(row[y_row])
  #y2.append(row[y2_row])
  c += 1

print("end line:%i" % (c - header_line + 1))

total_len = len(open(filepath).readlines())
print("total line:%i" % (total_len - header_line))

plt.xlabel("log_line")
plt.ylabel(data_title[y_row])

plt.plot(x,y)
#plt.plot(x,y2)

plt.show()
