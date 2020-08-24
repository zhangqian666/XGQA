# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-08-19 09:27
"""

from bert_base.client import BertClient
from models.qa_ner import *
from gstore.qa_query import *


def question_classif(question):
    bc = BertClient(port=7000, port_out=7001, mode="CLASS")
    result = bc.encode([question])

    return result[0]["pred_label"]


def classification_process(question, ques_type):
    if ques_type is "simple_res":
        simple_res_process(question)
    elif ques_type is "simple_res_reverse":
        simple_res_reverse_process(question)
    elif ques_type is "mult_constraints_one_simple":
        mult_constraints_one_simple_process(question)
    else:
        return "暂未解决该类问题 {}".format(ques_type)


def mult_constraints_one_simple_process(question):
    print("start mult_constraints_one_simple_parse -- >")

    ner_candi_list = ner_on_work(question)

    print(ner_candi_list)

    if len(ner_candi_list) == 0:
        return "未识别到实体"

    ner_candi_res = ner_candi_list[0][1]

    normal_query_entity_end = find_candi_entity(ner_candi_res)
    if len(normal_query_entity_end) == 0:
        return "未查到合适的对应实体"
    model = Model()

    print("通过字典查询到的候选实体  ： {}".format(normal_query_entity_end))

    true_entity = normal_query_entity_end[0]

    print("消歧后的实体  ： {}".format(true_entity))

    gstore_query_attr_end = model.query_attribute_mult_constraints_one_simple(true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(gstore_query_attr_end))

    true_attr = disambiguation_mult(question, ner_candi_res, gstore_query_attr_end)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end = model.query_answer_mult_constraints_one_simple(true_entity, true_attr)

    print("查询到的结果 : {}".format(answer_end))
    print("end mult_constraints_one_simple_parse -- >")
    return answer_end


def simple_res_reverse_process(question):
    print("start simple_res_reverse_parse -- >")

    ner_candi_list = ner_on_work(question)

    print(ner_candi_list)

    if len(ner_candi_list) == 0:
        return "未识别到实体"

    ner_candi_res = ner_candi_list[0][1]

    normal_query_entity_end = find_candi_entity(ner_candi_res)
    if len(normal_query_entity_end) == 0:
        return "未查到合适的对应实体"
    model = Model()

    print("通过字典查询到的候选实体  ： {}".format(normal_query_entity_end))

    #             true_entity = disambiguation_entity(question,normal_query_entity_end)
    true_entity = normal_query_entity_end[0]

    print("消歧后的实体  ： {}".format(true_entity))

    gstore_query_attr_end = model.query_attribute_simple_src(true_entity)
    print("通过gstore查询到的候选属性  ： {}".format(gstore_query_attr_end))

    true_attr = disambiguation(question, ner_candi_res, gstore_query_attr_end)
    print("消歧后的属性  ： {}".format(true_attr))

    answer_end = model.query_answer_simple_res_reverse(true_entity, true_attr)
    print("查询到的结果 : {}".format(answer_end))

    print("end simple_res_reverse_parse -- >")
    return answer_end


def simple_res_process(question):
    print("start simple_res_parse -- >")

    ner_candi_list = ner_on_work(question)

    print(ner_candi_list)
    if len(ner_candi_list) == 0:
        return "未识别到实体"

    ner_candi_res = ner_candi_list[0][1]

    normal_query_entity_end = find_candi_entity(ner_candi_res)
    if len(normal_query_entity_end) == 0:
        return "未查到合适的对应实体"
    model = Model()

    print("通过字典查询到的候选实体  ： {}".format(normal_query_entity_end))

    #             true_entity = disambiguation_entity(question,normal_query_entity_end)
    true_entity = normal_query_entity_end[0]

    print("消歧后的实体  ： {}".format(true_entity))

    gstore_query_attr_end = model.query_attribute_simple_src(true_entity)
    print("通过gstore查询到的候选属性  ： {}".format(gstore_query_attr_end))

    true_attr = disambiguation(question, ner_candi_res, gstore_query_attr_end)
    print("消歧后的属性  ： {}".format(true_attr))

    answer_end = model.query_answer_simple_src(true_entity, true_attr)
    print("查询到的结果 : {}".format(answer_end))

    print("end simple_res_parse -- >")
    return answer_end
