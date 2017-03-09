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
female=open("female.txt");

# 先为原始数据打好标签
#注意要把read出来的Unicode字符转换为utf-8字符串.................
labeled_names = ([(name.encode("utf-8") , 'male') for name in malefile.readlines()] + [(name.encode("utf-8"), 'female') for name in female.readlines()])
#labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
# 随机打乱打好标签的数据集的顺序，
random.shuffle(labeled_names)
# 从原始数据中提取特征（名字的最后一个字母， 参见gender_features的实现）
featuresets = [(gender_features(name), gender) for (name, gender) in labeled_names]
# 将特征集划分成训练集和测试集
train_set, test_set = featuresets[500:], featuresets[:500]
classif = NLTKClassifier(train_set)
classif.nltk_class = nltk.NaiveBayesClassifier;
blob = TextBlob("man", classifier=classif)
print blob.classify()