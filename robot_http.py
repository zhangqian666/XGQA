# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2021-01-11 22:11
"""
from flask import jsonify, Flask, request, render_template

app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


@app.route('/predict', methods=["POST", "GET"])
def predict():
    question = request.values.get("message")
    sn = request.values.get("sn")
    appid = request.values.get("appid")
    lang = request.values.get("lang")
    if (question is None) or (question is ""):
        return jsonify(data="问题不能为空")

    actionList = []

    action = {
        "command": "speech",
        "parameters": {
            "text": "请您对以下问题进一步选择，回复相应编号"
        },
        "datas": [
            {
                "answer": "1. 将充电线的USB插头插入计算机上的USB端口或任意USB充电器端口。\n2. 使用充电线上的磁吸端吸附到眼镜腿内侧的磁吸端。\n3. 确保充电电缆上的插脚与端口安全连接\n4. 在充电时眼镜的LED灯会1秒闪烁1次。",
                "answer_content_type": 0,
                "answer_model": 1,
                "weight": 1,
                "question_content": "如何给眼镜充电",
                "answer_content_url": "default",
                "pid": 308,
                "id": 2379

            }
        ]
    }
    actionList.append(action)

    return jsonify(status=True, responseCode="200", entry={
        "actionList": actionList,
        "seq": 1
    })


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8001, debug=True)
