# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-11 09:19
"""

import re

type_name = "mult_constraints_three_simple"
with open("/Users/zhangqian/PycharmProjects/XGQA/assert/train_data/task1-4_train_2020.txt", "r", encoding="utf-8") as f:
    with open("/Users/zhangqian/PycharmProjects/XGQA/assert/train_data/" + type_name + ".tsv", "w+",
              encoding="utf-8") as f1:

        def end():
            question = ""
            for line in f.readlines():
                if line.startswith("select"):
                    # pattern = re.compile(r'\{ <.*?> \?. <.*?>. }')
                    pattern = re.compile(r'\?. <.*?> <.*?>')
                    pattern5 = re.compile(r'\{ <.*?> <.*?> \?.')
                    pattern2 = re.compile(r'\{ \?. <.*?> <.*?>. }')
                    pattern3 = re.compile(r'\?. <.*?> \".*"')
                    pattern4 = re.compile(r'\?. <.*?> \?.')
                    res = pattern.findall(line)
                    res2 = pattern2.findall(line)
                    res3 = pattern3.findall(line)
                    res4 = pattern4.findall(line)
                    res5 = pattern5.findall(line)
                    if len(res) == 1 and len(res4) == 1 and len(res5) == 0 and len(res3) == 1:
                        # if len(res) > 0:
                        print((question, line, len(res)))
                        f1.write("{}\t{}\t{}".format(type_name, question[0:-1], line))
                question = line


        def jump_one():
            question = ""
            for line in f.readlines():
                if line.startswith("select"):

                    # pattern = re.compile(r'select \?x where \{ <.*?> <.*?> \?y.*?\?y <.*?> \?x')
                    pattern = re.compile(r'select \?y where \{ <.*?> <.*?> \?x.*?\?x <.*?> \?y')
                    res = pattern.findall(line)

                    if len(res) == 1:
                        # if len(res) > 0:
                        print((question, line, len(res)))
                        f1.write("{}\t{}\t{}".format(type_name, question[0:-1], line))
                question = line


        def simple_attr2_mult_two2():
            question = ""
            for line in f.readlines():
                if line.startswith("select"):
                    # pattern = re.compile(r'\{ <.*?> \?. <.*?>. }')
                    pattern = re.compile(r'\{ <.*?> <.*?> \?.. <.*')
                    pattern2 = re.compile(r'\?. <.*?> <.*?>.')
                    pattern3 = re.compile(r'\?x <.*?> \".*"')
                    pattern4 = re.compile(r'\?. <.*?> \?.')
                    res = pattern.findall(line)
                    res2 = pattern2.findall(line)
                    res3 = pattern3.findall(line)
                    res4 = pattern4.findall(line)
                    if len(res) > 0 and len(res2) == 0 and len(res3) == 0 and len(res4) == 0:
                        # if len(res) > 0:
                        print((question, line, len(res)))
                        f1.write("{}\t{}\t{}".format(type_name, question[0:-1], line))
                question = line


        def simple_attr_res_mult_c_two_three():
            question = ""
            for line in f.readlines():
                if line.startswith("select"):
                    # pattern = re.compile(r'\{ <.*?> \?. <.*?>. }')
                    pattern = re.compile(r'\?. <.*?> <.*?>')
                    pattern2 = re.compile(r'\{ \?. <.*?> <.*?>. }')
                    pattern3 = re.compile(r'\?x <.*?> \".*"')
                    pattern4 = re.compile(r'\?. <.*?> \?.')
                    res = pattern.findall(line)
                    res2 = pattern2.findall(line)
                    res3 = pattern3.findall(line)
                    res4 = pattern4.findall(line)
                    if len(res) == 3 and len(res4) == 1:
                        # if len(res) > 0:
                        print((question, line, len(res)))
                        f1.write("{}\t{}\t{}".format(type_name, question[0:-1], line))
                question = line


        simple_attr_res_mult_c_two_three()
