# -*- coding: utf-8 -*-

"""
@author: zhangqian

@contact: 

@Created on: 2020-07-12 14:29
"""
from gstore.GstoreConnector import GstoreConnector
import json


class Model():

    def make_query(self, query_content):
        gstoreConnector = GstoreConnector("gstore9001.ngrok.apex.ac.cn", 6060, "root", "123456")
        return gstoreConnector.query("pku", "json", query_content)

    def parse_json_attr(self, json_str):

        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['p']
                res1 = res1['value']

                if res1 not in end_ls:
                    end_ls.append(res1)
        except:
            print("解析错误/或者数据为空")
        return end_ls

    def parse_json_two_attr(self, json_str):

        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['p']
                res1 = res1['value']
                res2 = res["p1"]
                res2 = res2["value"]
                if (res1, res2) not in end_ls:
                    end_ls.append([res1, res2])
        except:
            print("解析错误/或者数据为空")
        return end_ls

    def parse_json_three_attr(self, json_str):

        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['p']
                res1 = res1['value']
                res2 = res["p1"]
                res2 = res2["value"]
                res3 = res["p2"]
                res3 = res3["value"]
                if (res1, res2, res3) not in end_ls:
                    end_ls.append([res1, res2, res3])
        except:
            print("解析错误/或者数据为空")
        return end_ls

    def parse_json_answer(self, json_str):
        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['x']
                res_type = res1["type"]
                res_value = res1['value']

                if res_type == "literal":
                    res_value = r'"%s"' % res_value
                elif res_type == "uri":
                    res_value = r'<%s>' % res_value

                if res_value not in end_ls:
                    end_ls.append(res_value)


        except:
            print("解析错误/或者数据为空")
        return end_ls

    #################   simple_src    #################

    def query_attribute_simple_src(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
        select distinct ?p where { <%s> ?p ?r.}
                """ % entity

        return self.parse_json_attr(self.make_query(query))

    def query_answer_simple_src(self, entity, attribute):
        current_query = r'select distinct ?x where {<%s> <%s> ?x . }' % (
            entity, attribute)

        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   simple_res_reverse    #################

    def query_attribute_simple_res_reverse(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
        select distinct ?p where {?x ?p <%s>.}
                """ % entity

        return self.parse_json_attr(self.make_query(query))

    def query_answer_simple_res_reverse(self, entity, attribute):
        current_query = r'select distinct ?x where {?x <%s> <%s> . }' % (
            attribute, entity)
        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   mult_constraints_one_simple    #################

    def query_attribute_mult_constraints_one_simple(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
        select distinct ?p ?p1 where {<%s> ?p ?r. ?r ?p1 ?r2.}
                """ % entity

        return self.parse_json_two_attr(self.make_query(query))

    def query_answer_mult_constraints_one_simple(self, entity, attribute):
        current_query = r'select distinct ?x where {<%s> <%s> ?r . ?r <%s> ?x . }' % (
            entity, attribute[0], attribute[1])

        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   mult_constraints_one_simple    #################

    def query_attribute_mult_constraints_one_reverse_simple(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select distinct ?p ?p1
                  where {
                        ?x ?p <%s>. 
                        ?x ?p1 ?y. 
                      }
                """ % entity

        return self.parse_json_two_attr(self.make_query(query))

    def query_answer_mult_constraints_one_reverse_simple(self, entity, attribute):
        current_query = r'select distinct ?x where {?r <%s> <%s> . ?r <%s> ?x . }' % (
            attribute[0], entity, attribute[1])

        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   mult_constraints_two_reverse    #################

    def query_attribute_mult_constraints_two_reverse(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select distinct ?p ?p1 where {
                   ?x ?p <%s>. 
                   ?x ?p1 <%s>. 
                   }
                """ % (entity[0], entity[1])

        return self.parse_json_two_attr(self.make_query(query))

    def query_answer_mult_constraints_two_reverse(self, entity, attribute):
        current_query = r'select distinct ?x where {?x <%s> <%s> . ?x <%s> <%s> . }' % (
            attribute[0], entity[0], attribute[1], entity[1])

        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   mult_constraints_two_reverse_simple    #################

    def query_attribute_mult_constraints_two_reverse_simple(self, entity):
        """
                select ?y where { ?x <原著> <马里奥·普佐>. ?x <主演> <马龙·白兰度>. ?x <上映时间> ?y. }
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select distinct ?p ?p1 ?p2 where {
                   ?x ?p <%s>. 
                   ?x ?p1 <%s>. 
                   ?x ?p2 ?y
                   }
                """ % (entity[0], entity[1])

        return self.parse_json_three_attr(self.make_query(query))

    def query_answer_mult_constraints_two_reverse_simple(self, entity, attribute):
        current_query = r'select distinct ?x where {?x <%s> <%s> . ?x <%s> <%s> . ?x <%s> ?y . }' % (
            attribute[0], entity[0], attribute[1], entity[1], attribute[2])

        return self.parse_json_answer(self.make_query(current_query)), current_query

    #################   mult_constraints_three_reverse    #################
    def query_attribute_mult_constraints_three_reverse(self, entity):
        """
                      获取实体的所有属性
                      :param entity:
                      :return:

                      """
        query = """
                        select distinct ?p ?p1 ?p2 where {
                         ?x ?p <%s>. 
                         ?x ?p1 <%s>. 
                         ?x ?p2 <%s>
                         }
                      """ % (entity[0], entity[1], entity[2])

        return self.parse_json_three_attr(self.make_query(query))

    def query_answer_mult_constraints_three_reverse(self, entity, attribute):
        current_query = r'select distinct ?x where {?x <%s> <%s> . ?x <%s> <%s> . ?x <%s> <%s> . } ' % (
            attribute[0], entity[0], attribute[1], entity[1], attribute[2], entity[2])

        return self.parse_json_answer(self.make_query(current_query)), current_query
