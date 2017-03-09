#encoding=utf-8
from snownlp import SnowNLP
import json
"""
情感分析，正负面分析
"""
text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
'''

s = SnowNLP(text)


#情感分析，小于0.5为消极，大于0.5为积极
print  s.sentiments