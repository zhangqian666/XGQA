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

    return result[0]["pred_label"][0]


def classification_process(question, ques_type):
    if ques_type == "simple_res":
        return simple_res_process(question, ques_type)
    elif ques_type == "simple_res_reverse":
        return simple_res_reverse_process(question, ques_type)
    elif ques_type == "mult_constraints_one_simple":
        return mult_constraints_one_simple_process(question, ques_type)
    elif ques_type == "mult_constraints_one_reverse_simple":
        return mult_constraints_one_reverse_simple_process(question, ques_type)
    elif ques_type == "mult_constraints_two_reverse":
        return mult_constraints_two_reverse_process(question, ques_type)
    elif ques_type == "mult_constraints_two_reverse_simple":
        return mult_constraints_two_reverse_simple_process(question, ques_type)
    elif ques_type == "mult_constraints_three_reverse":
        return mult_constraints_three_reverse_process(question, ques_type)
    else:
        return "暂未解决该类问题 {}".format(ques_type)


def mult_constraints_three_reverse_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 3:
        return "识别实体数量错误"

    false_entity = false_entity_list
    true_entity = true_entity_list

    model = Model()

    false_attr = model.query_attribute_mult_constraints_three_reverse(
        true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation_mult(question, false_entity, false_attr)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_mult_constraints_three_reverse(
        true_entity,
        true_attr)

    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))

    return answer_end


def mult_constraints_two_reverse_simple_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 2:
        return "识别实体数量错误"

    false_entity = false_entity_list
    true_entity = true_entity_list

    model = Model()

    false_attr = model.query_attribute_mult_constraints_two_reverse_simple(
        true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation_mult(question, false_entity, false_attr)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_mult_constraints_two_reverse_simple(
        true_entity,
        true_attr)

    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))

    return answer_end


def mult_constraints_two_reverse_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 2:
        return "识别实体数量错误"

    false_entity = false_entity_list
    true_entity = true_entity_list

    model = Model()

    false_attr = model.query_attribute_mult_constraints_two_reverse(
        true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation_mult(question, false_entity, false_attr)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_mult_constraints_two_reverse(
        true_entity,
        true_attr)

    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))

    return answer_end


def mult_constraints_one_reverse_simple_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 1:
        return "识别实体数量错误"

    false_entity = false_entity_list[0]
    true_entity = true_entity_list[0]

    model = Model()

    gstore_query_attr_end = model.query_attribute_mult_constraints_one_reverse_simple(true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(gstore_query_attr_end))

    if len(gstore_query_attr_end) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation_mult(question, [false_entity], gstore_query_attr_end)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_mult_constraints_one_reverse_simple(true_entity, true_attr)

    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))
    return answer_end


def mult_constraints_one_simple_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 1:
        return "识别实体数量错误"

    false_entity = false_entity_list[0]
    true_entity = true_entity_list[0]

    model = Model()

    false_attr = model.query_attribute_mult_constraints_one_simple(true_entity)

    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation_mult(question, [false_entity], false_attr)

    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_mult_constraints_one_simple(true_entity, true_attr)

    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))
    return answer_end


def simple_res_reverse_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 1:
        return "识别实体数量错误"

    false_entity = false_entity_list[0]
    true_entity = true_entity_list[0]

    model = Model()

    false_attr = model.query_attribute_simple_src(true_entity)
    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation(question, false_entity, false_attr)
    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_simple_res_reverse(true_entity, true_attr)
    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))
    return answer_end


def simple_res_process(question, ques_type):
    print("start {} parse -- >".format(ques_type))

    false_entity_list, true_entity_list = entity_normal_fun(question)

    if len(true_entity_list) != 1:
        return "识别实体数量错误"

    false_entity = false_entity_list[0]
    true_entity = true_entity_list[0]

    model = Model()

    false_attr = model.query_attribute_simple_src(true_entity)
    print("通过gstore查询到的候选属性  ： {}".format(false_attr))

    if len(false_attr) == 0:
        return "未查到合适的候选属性"

    true_attr = disambiguation(question, false_entity, false_attr)
    print("消歧后的属性  ： {}".format(true_attr))

    answer_end, current_query = model.query_answer_simple_src(true_entity, true_attr)
    print("查询到的结果 : {}".format(answer_end))

    print("end {}   parse -- >".format(ques_type))

    return answer_end


def entity_normal_fun(question):
    entity_list = ner_on_work(question)
    print(entity_list)

    true_entity_list = []
    false_entity_list = []

    for ner in entity_list:
        false_entity = ner[1]
        normal_query_entity_end = find_candi_entity(false_entity)
        if len(normal_query_entity_end) == 0:
            continue

        print("通过字典查询到的候选实体  ： {}".format(normal_query_entity_end))

        true_entity = disambiguation_entity(question, normal_query_entity_end)
        print("消歧后的实体  ： {}".format(true_entity))

        true_entity_list.append(true_entity)
        false_entity_list.append(false_entity)

    return false_entity_list, true_entity_list


def end_process(question, answer_end, current_query):
    with open("./answer.txt", "a+", encoding="utf-8") as f:
        f.write("{}\n{}\n{}\n\n".format(question, current_query, answer_end))
