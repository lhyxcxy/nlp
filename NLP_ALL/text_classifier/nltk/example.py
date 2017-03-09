# -*- coding: utf-8 -*-
import json
import codecs
import jieba
from sklearn.cluster import KMeans
import uuid
from jieba import analyse
import  nltk
from snownlp import SnowNLP
from numpy import array

#[array,array] list.append(numpy.array)
datas=[array(v) for v in [(1,0),(0,1),(5,5),(5,4),(5,3)]] #句子的分词向量，是一个numpy.array的list

km=nltk.cluster.kmeans.KMeansClusterer(num_means=2, distance =nltk.cluster.euclidean_distance)
km.cluster(datas)
for data in datas:
    print str(data)+str(km.classify(data))