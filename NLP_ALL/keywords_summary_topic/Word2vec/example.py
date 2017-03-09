# -*- coding: utf-8 -*-
from gensim import corpora
from collections import defaultdict
from gensim.models.tfidfmodel import TfidfModel
from gensim.models import *
import codecs
import json
import jieba;


def getToipc(file_name,toipc_type="lda",topics_num=5,topics_words=5):
    """
    生成主题模型
    :param file_name:
    :param toipc_type: lda or lsi
    :param topics_num:
    :param topic_words:
    :return:
    """
    texts=list()
    f = codecs.open(file_name, 'r')
    for line in f:
        tt_texts=list()
        line=line.strip()
        words=jieba.cut(line,cut_all=False)
        t_texts=list(words);
        for text in t_texts:
            if len(text.strip())>1:
                tt_texts.append(text)
        texts.append(tt_texts)


    # 去掉只出现一次的单词
    frequency = defaultdict(int)
    """for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]"""


    dictionary = corpora.Dictionary(texts)   # 生成词典# -*- coding: utf-8 -*-

    # 将文档存入字典，字典有很多功能，比如
    # diction.token2id 存放的是单词-id key-value对
    # diction.dfs 存放的是单词的出现频率
    dictionary.save('deerwester.dict')  # store the dictionary, for future reference
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('deerwester.mm', corpus)  # store to disk, for later use
    tfidf = TfidfModel(corpus)
    tfidf_corpus = tfidf[corpus]
    #print(tfidf.idfs)
    tfidf.save('foo.tfidf_model')

    """
    加载模型
    dictionary = corpora.Dictionary.load('mydict.dic')
    corpus = corpora.MmCorpus('lsi_corpus.mm')
    model = LsiModel.load('model.lsi')
    model2 = LdaModel.load('model.lda')
    TfidfModel.load(foo.tfidf_model)"""


    if toipc_type == "lsi":
        #lsi
        #lsi = LsiModel(corpus = tfidf_corpus,id2word=dictionary,num_topics=2)
        lsi = LsiModel(corpus = tfidf_corpus,id2word=dictionary)
        lsi_corpus = lsi[tfidf_corpus]
        lsi.save('model.lsi')
        corpora.MmCorpus.serialize('lsi_corpus.mm', lsi_corpus)
        #print 'LSI Topics:'
        #print json.dumps(lsi.print_topics(num_topics=topics_num,num_words=topics_words), encoding="UTF-8", ensure_ascii=False)
        return lsi.print_topics(num_topics=topics_num,num_words=topics_words)

    if toipc_type=="lda":
        #lda
        #lda = LdaModel(corpus = tfidf_corpus,id2word=dictionary,num_topics=1)
        lda = LdaModel(corpus = tfidf_corpus,id2word=dictionary)
        lda_corpus = lda[tfidf_corpus]
        lda.save('model.lda')
        corpora.MmCorpus.serialize('lda_corpus.mm', lda_corpus)
        #print 'LDA Topics:'
        #print json.dumps(lda.print_topics(num_topics=topics_num,num_words=topics_words), encoding="UTF-8", ensure_ascii=False)
        return lda.print_topics(num_topics=topics_num,num_words=topics_words);

#print corpus
#print dictionary
#print dictionary.token2id

print json.dumps(getToipc("text1.txt",topics_num=1), encoding="UTF-8", ensure_ascii=False)