# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-05-10 13:07
"""


def get_question_list(url):
    with open(url, "r", encoding="utf-8") as f:
        questions = []
        for question in f:
            question_striped = question.strip()
            questions.append(question_striped)
        return questions


