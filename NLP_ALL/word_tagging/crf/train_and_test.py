#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

import CRFPP

"""
训练载crf++中使用如下命令
注意：template是模板文件，curpus.txt为两字段的一语料库，crf_model_1 为生成的训练文件
crf_learn -f 3 -c 1.5 ./template ./curpus.txt  crf_model_1 -t

参数如下:
可选参数
-f, –freq=INT使用属性的出现次数不少于INT(默认为1)
-m, –maxiter=INT设置INT为LBFGS的最大迭代次数 (默认10k)
-c, –cost=FLOAT      设置FLOAT为代价参数，过大会过度拟合 (默认1.0)
-e, –eta=FLOAT设置终止标准FLOAT(默认0.0001)
-C, –convert将文本模式转为二进制模式
-t, –textmodel为调试建立文本模型文件
-a, –algorithm=(CRF|MIRA)
选择训练算法，默认为CRF-L2
-p, –thread=INT线程数(默认1)，利用多个CPU减少训练时间
-H, –shrinking-size=INT
设置INT为最适宜的跌代变量次数 (默认20)
-v, –version显示版本号并退出
-h, –help显示帮助并退出
"""

def getCx(content_words):
    """
    得到词性
    :param content_words:注意 单词是按照在句子中的顺序排列的
    :return: 返回对应的单词的tag
    """
    tags=list()
    try:
        tagger = CRFPP.Tagger("-m " + "crf_model_1")
        tagger.clear()
        for word in content_words:
            word = word.strip()
            if word:
                tagger.add(word.encode('utf-8'))
        tagger.parse()
        size = tagger.size()#tagger.add的数据大小
        xsize = tagger.xsize()
        for i in range(0, size):
            for j in range(0, xsize):
                #char = tagger.x(i, j).decode('utf-8')
                tag = tagger.y2(i)
                tags.append(tag)
    except RuntimeError, e:
        print "RuntimeError: ", e,
    return tags
print getCx(["中国","与" ,"周边" ,"国家" ,"和","广大","发展中国家","的","友好","合作","进一步","加强"])
