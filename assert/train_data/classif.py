# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-14 18:08
"""
import random

with open("/Users/zhangqian/jupyer-notebookproject/XGQA/assert/train_data/" + "dev" + ".tsv", "r",
          encoding="utf-8") as f:
    question = ""
    numlist = []
    for line in f.readlines():
        numlist.append(line)

    random.shuffle(numlist)

    with open("/Users/zhangqian/jupyer-notebookproject/XGQA/assert/train_data/" + "dev1" + ".tsv", "w",
              encoding="utf-8") as f1:

        for line1 in numlist:
            f1.write(line1)

    # str = line.split("\t")[1]
    #
    # # print("{} ----- {} ".format(str, num))
    # if str not in numlist:
    #     numlist.append(str)
    #
    # else:
    #     print("重复数据： --------------------》  {}", format(str))
    #
