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
    list = []
    i=0;
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
        app[u"问题"]=question;
        app[u"答案"]= answer
        list.append(app)
    return list


def getFenCiWords():
    """
    得到分词后单词，及对应的原始文档
    :return:
    """
    tfidf = analyse.extract_tags
    allwordsList = loadFile();
    aList = []
    stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines()]
    stop_baoxian = [line.strip().decode('utf-8') for line in open('stop_baoxian.txt').readlines()]
    s2 = set(stop);
    s2_1 = set(stop_baoxian)
    s2 = s2 | s2_1
    for index in range(len(allwordsList)):
        wenti1 = allwordsList[index][u'问题']
        qa = allwordsList[index][u'问题'] + " " + allwordsList[index][u'答案']
        keywords = tfidf(wenti1)
        ks = []
        for wo in keywords:
            if (wo in s2) != True:
                ks.append(wo)
        allwordsList[index]["label"] = ks
        ywords = jieba.cut(wenti1, cut_all=True)
        s1 = set();
        for word in ywords:
            s1.add(word)
        words = list(s1 - s2);
        word_str = ""
        for key in words:
            word_str = word_str + key + " "
        aList.insert(index, word_str)
        print word_str
    return aList, allwordsList  # 第一个参数为分词结果，第二列参数为原始文档

def getTFIDF():
    """

    :return:
    """
    corpus,textList=getFenCiWords();
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    print "共" + str(len(weight)) + "个文本" + ",共" + str(len(word)) + "个词"
    return weight, textList
    # for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    #   print u"-------这里输出第",i,u"类文本的词语tf-idf权重------"
    # for j in range(len(word)):
    # print word[j],weight[i][j]



def getCU(leibieNum):
    """
    聚类
    :param leibieNum: 聚的类别数目
    :return:
    """
    LEIBI=leibieNum    #100个类别
    #print "####################Start Kmeans:分成"+str(LEIBI)+"个类"
    weight, textList = getTFIDF()
    clf = KMeans(n_clusters=LEIBI)

   # s = clf.fit(weight)
    i = 1
    textFencuList=[]
    for i in range(0,LEIBI):
        textFencu2=[]
        textFencuList.append(textFencu2)
    for i in range(len(clf.labels_)):
        try:
            textFencuList[clf.labels_[i - 1]].append(textList[i])
        except Exception, e:
            print "#######错误："+str(clf.labels_[i - 1])+"  "+str(i)
    for index in range(len(textFencuList)):

        allLabels=[]
        for ab in textFencuList[index]:
            thisLabels=ab["label"]
            allLabels=allLabels+thisLabels;
        moreLabelList=Counter(allLabels).most_common(1)
        moreLabel=moreLabelList[0][0]
        moreLabelNum=moreLabelList[0][1]
        print ""
        print "#############################第" + str(index) + "个分类 " + moreLabel +"  " +str(moreLabelNum)+"开始##################";
        fileurl=("/home/lhy/data/aidata/"+moreLabel+"_"+str(uuid.uuid1())+".txt").encode("utf-8");
        print "#########################写入文件 ： "+fileurl
        fo2=codecs.open(fileurl, 'wb', encoding='utf-8')
        for ab in textFencuList[index]:
            labes=' '.join(ab["label"])
            line="if["+labes+"]then"+ab[u"答案"]
            fo2.writelines(line)
            fo2.writelines("\r\n")
        fo2.writelines("end")
        fo2.close()
        print "#############################" + moreLabel +"  " +str(moreLabelNum)+"分类结束##################";
        print ""
        # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    print("############评估因子大小，用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数：类别"+str(LEIBI)+"    因子"+str(clf.inertia_))
getCU(100)