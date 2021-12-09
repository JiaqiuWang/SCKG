"""
功能描述：Natural Language Processing With Neo4j - Mining Paradigmatic Word Associations
（基于Python与Neo4j的自然语言理解--挖掘文本数据中的关联词）
运行环境：Python 3.5+，Neo4j 3.1+
Label:自然语言理解, NLP, NLU, 知识图谱, 问答
作者：王佳秋
日期：2021年4月2日 push to github
网址：https://lyonwj.com/blog/nlp-with-neo4j
"""

import os
import string
import re
from py2neo import Graph


# Create a neo4j session
graph = Graph("http://127.0.0.1:7474", username="neo4j", password="123456")
print("graph:", graph)


def reset_db():
    """remove all nodes and relationships from the database"""
    graph.run("match (n) detach delete n")

def arrifySentence(sentence):
    """对句子进行序列化"""
    sentence = sentence.lower()  # 小写
    sentence = sentence.strip()  # 去掉空格
    exclude = set(string.punctuation)  # 标点符号不重复的集合
    print("exclude:", exclude)
    regex = re.compile('[%s]' % re.escape(string.punctuation))  # re.escape(pattern) 可以对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数。
    sentence = regex.sub('', sentence)  # 去掉特殊字符和标点符号，只保留文字
    print("sentence:", sentence)
    wordArray = sentence.split(" ")  # 获取字符数组
    print("wordArray:", wordArray)
    tupleList = []
    for i, word in enumerate(wordArray):
        print("i:", i, ", word:", word)
        if i+1 == len(wordArray):
            break
        tupleList.append([word, wordArray[i+1]])
    print("tupleList:", tupleList)
    return tupleList


def insertDB(tupleList):
    """单词对插入Neo4j  Given a query, create a graph based on each triple in the extracted statements"""
    for each in tupleList:
        print("each:", each, ", type:", type(each))
        query = '''
            MERGE (s:Word {name: $subject})
            MERGE (o:Word {name: $object})
            CREATE (s)-[:NEXT_WORD]->(o)
        '''
        graph.run(query, subject=each[0], object=each[1])





path = "Dataset"  # 文件夹目录
files = os.listdir(path)  # 得到在Path路径下所有文件名称列表
print("files:", files)  # list类型
reset_db()  # 清空原来的数据库
s = []
for file in files:
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        with open(path+'/'+file, 'r', encoding='utf-8') as f:
            count = 0
            print("type-f:", f)
            for line in f.readlines():
                print("line:", line.strip())
                print("Type-line:", type(line))
                insertDB(arrifySentence(line))













