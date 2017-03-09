#encoding=utf-8
from snownlp import SnowNLP
import json
import jieba;
"""
文本句子相似性
"""
#两篇文档
text1 = u'''我爱 中国 美国'''
text2=u'''北京 香港 美国'''
text3=u'''河南 河北'''

text_words1 = jieba.cut(text1,cut_all=True)
text_words2 = jieba.cut(text2,cut_all=True)
text_words3 = jieba.cut(text3,cut_all=True)

#测试数据
text_test = u'''我爱中国'''
test_words1=jieba.cut(text_test,cut_all=True)
test_words=list(test_words1);

text_words=[list(text_words1),list(text_words2),list(text_words3)]

#print " ".join(text_words)
s = SnowNLP(text_words)# 必须是分好词的文档如：[[我爱, 中国, 美国,],[北京,香港,美国],[河南,河北]]

#tf=某个词在本文档中出现的次数/本文档的总词数  [{"我": 1, "爱": 1, "中国": 1, "美国": 1, "": 4}, {"": 4, "北京": 1, "美国": 1, "香港": 1}, {"": 2, "河北": 1, "河南": 1}]
print json.dumps(s.tf, encoding="UTF-8", ensure_ascii=False)

#idf=log(语料库文档总数/(包含该词的文档数+1)) {"": -1.9459101490553135, "我": 0.5108256237659907, "香港": 0.5108256237659907, "河南": 0.5108256237659907, "北京": 0.5108256237659907, "河北": 0.5108256237659907, "爱": 0.5108256237659907, "美国": -0.5108256237659907, "中国": 0.5108256237659907}
print json.dumps(s.idf, encoding="UTF-8", ensure_ascii=False)
#输出  [1.3702146143370104, 0, 0] 表示与第一类相似
print json.dumps(s.sim(test_words), encoding="UTF-8", ensure_ascii=False)

