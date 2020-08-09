# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-05-10 16:04
"""

from gstore.GstoreConnector import *

gstoreConnector = GstoreConnector("gstore.ngrok.apex.ac.cn", 6060, "root", "123456")

# sparql = "SELECT ?x ?y WHERE {<蓬门今始为君开亲情友情篇（精）> ?x ?y}"
# sparql = "SELECT ?x ?y WHERE {<ASP.NETXML深入编程技术（编程宝典2002）> ?x ?y}"
# sparql = "SELECT ?x ?y WHERE {<观察作文（适用于34年级双色图解）> ?x ?y}"
# sparql = "SELECT ?x ?y WHERE {<当代回族音乐> ?x ?y}"
sparql = "SELECT ?x ?y WHERE {<复旦大学> ?x ?y .}"

answer = gstoreConnector.query("xg", "json", sparql)

print(answer)
