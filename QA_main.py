# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-05-10 12:50
"""

from utils.handle_word import *
from utils.url_manager import *

if __name__ == "__main__":
    questions = get_question_list(question_url)
    print(questions)
