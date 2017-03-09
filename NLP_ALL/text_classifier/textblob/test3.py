# coding=utf-8
import random, nltk
from nltk.corpus import names
from textblob.classifiers import NLTKClassifier
from textblob import TextBlob
import sys

"""
有监督的分类，训练男女姓名文件对男女名字进行分类
"""
def gender_features(word):
    '''''''提取每个单词的最后一个字母作为特征'''
    return {'last_letter': word[-1]}
malefile=open('male.txt');
x1=names.words('male.txt');
x2=list(malefile.readlines())
print " ".join(x1)