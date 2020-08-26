# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-26 11:05
"""
import random

with open("/Users/zhangqian/jupyer-notebookproject/XGQA/assert/ner_train_data/train_simple.txt", "r"
        , encoding="utf-8") as f:
    all_data = []
    temp_list = []
    for line in f.readlines():
        temp_list.append(line)
        if line == "\n":
            all_data.append(temp_list)
            temp_list = []

    random.shuffle(all_data)

    with open("/Users/zhangqian/jupyer-notebookproject/XGQA/assert/ner_train_data/train_all.txt", "w",
              encoding="utf-8") as f1:
        for lines in all_data:
            for line in lines:
                f1.write(line)
