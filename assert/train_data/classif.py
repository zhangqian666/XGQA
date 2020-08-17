# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-14 18:08
"""

with open("/Users/zhangqian/jupyer-notebookproject/XGQA/assert/classification_data/" + "all_data" + ".tsv", "r",
          encoding="utf-8") as f:
    question = ""
    numlist = []
    for line in f.readlines():
        str = line.split("\t")[1]

        num = str.split(":")[0][1:]
        num = int(num)
        # print("{} ----- {} ".format(str, num))
        if num not in numlist:
            numlist.append(num)
        else:
            print("重复数据： --------------------》  {}", format(num))

        numlist.sort()
    print(numlist)
