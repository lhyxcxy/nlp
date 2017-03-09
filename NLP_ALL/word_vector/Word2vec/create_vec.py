#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gensim.models import word2vec
import logging

"""
生成词向量
也可以载word2vec中使用命令，注意下命令生成的向量文件是c语言格式可读的
应该使用model = word2vec.Word2Vec.load_word2vec_format("wordvec_c.model", binary=True)#c 文件

./word2vec -train data/chinesewords.txt -output data/wordvec_c.model -cbow 1 -size 200 -window 8 -negative 0 -hs 1 -sample 1e-4 -threads 20 -binary 1 -iter 15

"""
# # 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"corpus.txt")
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

# 计算两个词的相似度/相关程度
y1 = model.similarity(u"主席", u"习近平")
print "【主席】和【习近平】的相似度为："+ str(y1)
print "--------\n"

# 计算某个词的相关词列表
y2 = model.most_similar(u"主席", topn=20)  # 20个最相关的
print "和【主席】最相关的词有：\n"
for item in y2:
    print str(item[0])+ str(item[1])
print "--------\n"

# 寻找对应关系
print u"与 ‘习近平 中国’相近，并排除 ‘主席’ 相关的词  "
y3 = model.most_similar([u'习近平', u'中国'], [u'主席'], topn=3)
for item in y3:
    print str(item[0])+ str(item[1])
print "--------\n"

# 寻找不合群的词
y4 = model.doesnt_match(u"习近平 中国  发展 手机".split())
print "'习近平 中国  发展 手机' 不合群的词："+y4
print "--------\n"

# 保存模型，以便重用,保存后会生成一个文件，里面存的是语料库的向量
model.save(u"wordvec.model")
# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")

# 以一种C语言可以解析的形式存储词向量
model.save_word2vec_format(u"wordvec_c.model", binary=True)
# 对应的加载方式
# model_3 = word2vec.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)

if __name__ == "__main__":
    pass