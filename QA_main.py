# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-05-10 12:50
"""

from utils.handle_word import *
from utils.url_manager import *
import time
from models.qa_classification import question_classif, classification_process
from models.qa_ner import *
from gstore.qa_query import *
import pandas as pd

if __name__ == "__main__":
    questions = get_question_list(question_url)


    for question in questions:
        classification = question_classif(question)

        answer = classification_process(question, classification)
