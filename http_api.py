# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2021-01-11 20:14
"""
from flask import jsonify, Flask, request
from models.qa_classification import *

app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


@app.route('/predict')
def predict():
    question = request.args.get("question")
    # question = "电影《沉默的羔羊》是一部什么类型的电影？"
    classification = question_classif(question)
    end_data = classification_process("1", question, classification)
    return jsonify(result=end_data)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8000, debug=True)
