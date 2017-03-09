# -*- coding: utf-8 -*-
import json
import codecs
import jieba
from sklearn.cluster import KMeans
import uuid
from jieba import analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

def loadFile():
    """
    加载文件
    :return:
    """
    f = codecs.open("data.json", 'r')

    sentences=list();
    sentences_words=list()
    for line in f:
        line=line[:-1]
        if line=="":
            continue
        app = {}
        line=line.encode("utf-8")
        try:
            setting = json.loads(line)
            question = setting['question']   #意多重结构的读取语法
            answer = setting['answer']
        except Exception, e:
            continue
        if question=="" or answer=="":
            continue
       # app[u"问题"]=question;
        #app[u"答案"]= answer
        words=list(jieba.cut(question,cut_all=True))
        wordsStr=" ".join(words)
        sentences.append(question)
        sentences_words.append(wordsStr)
    return sentences_words,sentences#分好词的句子，原始句子

def kmeans(class_num):
    """
    kmeans 分类
    :param class_num: 分类数量
    :return:class_list[[句子1，句子2],[句子1，句子2]]
    """
    class_list=list();
    sentences_words,sentences=loadFile()
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    #注意此处的words_list  必须是["我 爱 中国 天安门","北京 大学"] 样式的分好词并以空格分来的list
    tfidf = transformer.fit_transform(vectorizer.fit_transform(sentences_words))

    #weight 是一个shape=[句子数，分词数量] 组成的二维数组
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    clf = KMeans(n_clusters=class_num)
    s = clf.fit(weight)
    for i in range(class_num):
        class_list.append(list())
    print clf.labels_
    for i in range(len(clf.labels_)):#clf.labels_ 是每个句子所属的类别[1,3,2,5,0,3,5,4,1] 下标对应数据句子的下标
        class_label=clf.labels_[i]
        class_list[class_label].append(sentences[i])
        #print "#######第"+str(clf.labels_[i])+"类"+words_list[i]
    return class_list;

class_sentences=kmeans(3);
for i in range(len(class_sentences)):
    print "##############第"+str(i)+"类";
    for c1 in class_sentences[i]:
        print c1

