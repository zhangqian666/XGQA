# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-19 09:27
"""

from bert_base.client import BertClient


def question_classif(question):
    bc = BertClient(port=7000, port_out=7001, mode="CLASS")
    result = bc.encode([question])

    return result[0]["pred_label"]
