#coding:utf-8
from gensim import corpora,similarities,models
import os
import jieba

"""
计算句子和语料库中哪个句子相似
"""
# 首先加载语料库
if os.path.exists('lsi_corpus.mm') and os.path.exists('mydict.dict'):
    dictionary = corpora.Dictionary.load('mydict.dict')
    corpus = corpora.MmCorpus('lsi_corpus.mm')
    model = models.LsiModel.load('model.lsi')
    print 'used files generated from topics'
else:
    print 'please run topics firstly'

index = similarities.MatrixSimilarity(corpus)
index.save('lsi_similarity.sim')

document = u'当地时间18时许，习近平在第71届联合国大会主席汤姆森和联合国秘书长古特雷斯陪同下步入万国宫大会厅，全场起立，热烈鼓掌欢迎。'
bow_vec = dictionary.doc2bow(jieba.lcut(document))
lsi_vec = model[bow_vec]
sims = index[lsi_vec]  #余弦相似度
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sims
#[(2, 0.99584925), (15, 0.1355263), (1, 0.12038891), (0, 0.094309233), (17, 0.091441453), (14, 0.088668972), (12, 0.047591072), (16, 0.025794223), (4, 0.017965719), (8, 0.017394736), (3, 0.013194671), (13, 0.012415368), (5, 0.010290033), (6, 0.0080233691), (7, 0.0041918214), (10, 2.1420419e-08), (11, 1.8626451e-09), (9, -8.3819032e-09)]
#可以看到和下标为2的原始句子相似