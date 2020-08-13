# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-12 10:03
"""
import re

import pandas as pd

end_list = []
type_name = "simple_res"
index = 0
with open("/Users/zhangqian/PycharmProjects/XGQA/assert/train_data/" + type_name + ".tsv", "r", encoding="utf-8") as f:
    for line in f.readlines():
        if index == 0:
            index = 1
            continue
        pattern = re.compile("<.*?>")
        res = pattern.findall(line)
        end = res[0].split("_")[0][1:-1]
        end_list.append(end)

print(end_list)

data = pd.read_csv("/Users/zhangqian/PycharmProjects/XGQA/assert/train_data/" + type_name + ".tsv", delimiter="\t",
                   usecols=[1])

str_list = data.iloc[:, 0].values
print(str_list)


## 开始标注

def biaozhu(str_line, word):
    new_str = str_line

    new_str.replace(word, "B" + "O" * (len(word) - 1))
