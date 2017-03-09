#encoding=utf-8
from snownlp import SnowNLP

"""简体繁体互转"""
s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
print s.han

