#encoding=utf-8
from snownlp import SnowNLP

"""汉字转拼音"""
s = SnowNLP(u'这个东西真心很赞')
print s.pinyin        # [u'zhe', u'ge', u'dong', u'xi',
                #  u'zhen', u'xin', u'hen', u'zan']

