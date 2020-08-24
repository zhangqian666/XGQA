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

    def parse_json_entity(self, json_str):
        # print(json_str)
        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['x']
                res1 = res1['value']
                if res1 not in end_ls:
                    end_ls.append(res1)
        except:
            print("解析错误/或者数据为空")
        return end_ls

    def parse_json_attr(self, json_str):
        # print(json_str)

        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['x']
                res1 = res1['value']
                res2 = res["r"]
                res2 = res2["value"]
                if (res1, res2) not in end_ls:
                    end_ls.append([res1, res2])
        except:
            print("解析错误/或者数据为空")
        return end_ls

    def parse_json_two_attr(self, json_str):
        # print(json_str)

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

    def parse_json_answer(self, json_str):
        # print(json_str)
        all_part = json.loads(json_str)  # 读取所有文件内容
        end_ls = []
        try:
            results = all_part['results']  # 获取results标签下的内容
            results_bindings = results['bindings']  # 获取results标签下的bingdings内容
            # 定义一个list，将数据全部放到list中
            for res in results_bindings:
                res1 = res['x']
                res1 = res1['value']
                if res1 not in end_ls:
                    end_ls.append(res1)


        except:
            print("解析错误/或者数据为空")
        return end_ls

    #################   simple_src    #################
    def query_entity_simple_src(self, entity):
        """
        查询实体 用于实体消歧
        :param entity:
        :return:
        """

        query = """
                  select distinct ?x
                  where {
                      <%s> ?x ?res.
                  }
               """ % entity

        return self.parse_json_entity(self.make_query(query))

    def query_attribute_simple_src(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select distinct ?x ?r
                  where {
                      <%s> ?x ?r.
                  }
                """ % entity

        return self.parse_json_attr(self.make_query(query))

    def query_answer_simple_src(self, entity, attribute):
        current_query = """
          SELECT ?x WHERE {<%s> <%s> ?x . } 
        """ % (entity, attribute)

        return self.parse_json_answer(self.make_query(current_query))

    #################   simple_res_reverse    #################

    def query_entity_simple_res_reverse(self, entity):
        """
        查询实体 用于实体消歧
        :param entity:
        :return:
        """

        query = """
                  select distinct ?x
                  where {
                    ?x ?res <%s>.
                  }
               """ % entity

        return self.parse_json_entity(self.make_query(query))

    def query_attribute_simple_res_reverse(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select distinct ?x ?r
                  where {
                     ?x ?r <%s>.
                  }
                """ % entity

        return self.parse_json_attr(self.make_query(query))

    def query_answer_simple_res_reverse(self, entity, attribute):
        current_query = """
          SELECT ?x WHERE { ?x <%s> <%s>. } 
        """ % (attribute, entity)
        return self.parse_json_answer(self.make_query(current_query))

    #################   mult_constraints_one_simple    #################

    def query_attribute_mult_constraints_one_simple(self, entity):
        """
                获取实体的所有属性
                :param entity:
                :return:

                """
        query = """
                  select ?p ?p1
                  where {
                        <%s> ?p ?r.
                         ?r ?p1 ?r2 .
                      }
                """ % entity

        return self.parse_json_two_attr(self.make_query(query))

    def query_answer_mult_constraints_one_simple(self, entity, attribute):
        current_query = """
             SELECT ?x WHERE {<%s> <%s> ?r .
                                ?r <%s> ?x .
                                } 
           """ % (entity, attribute[0], attribute[1])

        return self.parse_json_answer(self.make_query(current_query))
