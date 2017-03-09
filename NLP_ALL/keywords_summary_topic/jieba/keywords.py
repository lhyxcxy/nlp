#encoding=utf-8
import jieba.analyse
"""jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
sentence 为待提取的文本
topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
withWeight 为是否一并返回关键词权重值，默认值为 False
allowPOS 仅包括指定词性的词，默认值为空，即不筛选
jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件"""

sentence="上海要统筹考虑国际发展趋势要求我们干什么、国家战略需要我们干什么、自身发展最需要突破什么。”中共中央政治局委员、上海市委书记韩正多次强调，谋划上海工作要有更大视野、始终把握大势，规划上海发展要把准定位、始终把中央指示要求作为贯穿一切的工作主线。“凡是有利于国家利益、大局发展的工作，我们要毫不迟疑地做，坚持不懈地抓；凡是中央确定的战略谋划、布局和任务，我们要主动承接、积极参与、自我加压；凡是符合创新、协调、绿色、开放、共享发展理念的事，我们要勇于率先探索、真抓实干"
keywords=jieba.analyse.extract_tags(sentence, topK=5, withWeight=False, allowPOS=())
print " ".join(keywords)