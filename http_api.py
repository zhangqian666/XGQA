# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2021-01-11 20:14
"""
from flask import jsonify, Flask, request, render_template
from models.qa_classification import *

app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


@app.route('/predict', methods=["POST", "GET"])
def predict():
    question = request.values.get("message")
    if (question is None) or (question is ""):
        return jsonify(data="问题不能为空")
    # question = "电影《沉默的羔羊》是一部什么类型的电影？"
    classification = question_classif(question)
    answer_end, false_entity, true_entity, false_attr, true_attr = simple_res_process("1", question, classification)
    end_data = "answer_end:{};" \
               "false_entity:{};" \
               "true_entity:{};" \
               "false_attr:{};" \
               "true_attr:{};".format(answer_end, false_entity, true_entity, false_attr, true_attr)

    return jsonify(data=end_data)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8000, debug=True)
