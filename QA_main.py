# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-05-10 12:50
"""

from utils.handle_word import *
from utils.url_manager import *
import time
from models.qa_classification import question_classif
from models.qa_ner import *
from gstore.qa_query import *
import pandas as pd

if __name__ == "__main__":
    questions = get_question_list(question_url)

    type_list = []
    for question in questions:
        end_classif = question_classif(question)
        if end_classif not in type_list:
            type_list.extend(end_classif)
