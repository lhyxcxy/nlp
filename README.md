# lhy-nlp

## 如果您喜欢，请点一下star,我会持续更新其他好玩的东西。
各种nlp 工具的使用包括 word2vec nltk textblob crf++ 等
<pre name="code" class="python">（1）机器人
（2）中文翻译，及繁体转简体
（3）关键词提取，主题提取，摘要提取
（4）命名体识别
（5）分词
（6）情感分析，正负类分析
（7）近义词，同义词，句子相似性
（8）聚类，监督，无监督
（9）词性标注
（10）词向量提取
.
├── chatbot   #########################机器人
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; └── readMe.txt
├── chinese_trans ################ 中文翻译，及繁体转简体
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; └── snowNlp
│&nbsp;&nbsp;     ├── chinese_to_fanti.py
│&nbsp;&nbsp;     ├── chinese_to_pinyin.py
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     └── readMe.txt
├── keywords_summary_topic  ###########关键词提取，主题提取，摘要提取
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── jieba
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; └── keywords.py
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; ├── snowNlp
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; └── keyword_summary.py
│&nbsp;&nbsp; └── Word2vec
│&nbsp;&nbsp;     ├── deerwester.dict
│&nbsp;&nbsp;     ├── deerwester.mm
│&nbsp;&nbsp;     ├── deerwester.mm.index
│&nbsp;&nbsp;     ├── example.py
│&nbsp;&nbsp;     ├── foo.tfidf_model
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     ├── lda_corpus.mm
│&nbsp;&nbsp;     ├── lda_corpus.mm.index
│&nbsp;&nbsp;     ├── lsi_corpus.mm
│&nbsp;&nbsp;     ├── lsi_corpus.mm.index
│&nbsp;&nbsp;     ├── model.lda
│&nbsp;&nbsp;     ├── model.lda.expElogbeta.npy
│&nbsp;&nbsp;     ├── model.lda.id2word
│&nbsp;&nbsp;     ├── model.lda.state
│&nbsp;&nbsp;     ├── model.lsi
│&nbsp;&nbsp;     ├── model.lsi.projection
│&nbsp;&nbsp;     ├── text1.txt
│&nbsp;&nbsp;     ├── text2.txt
│&nbsp;&nbsp;     └── text3.txt
├── named\ _entity_\ recognition #################命名体识别
│&nbsp;&nbsp; ├── crf
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── 199801.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── create_corpus.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── crf_model_1
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── curpus.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── doc.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; └── train_and_test.py
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; └── readMe.txt
├── participle       ########################分词
│&nbsp;&nbsp; ├── crf
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── 199801.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── crf_model
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── crf_model_1
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── setp_1.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── setp_2.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── test_input.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── test_output.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; └── train.data
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── jieba
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── fenci.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── stopdict.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; └── userdict.txt
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; └── snowNlp
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     └── words_sentences.py
├── sentiment_analysis ###########################情感分析，正负类分析
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; └── snowNlp
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     └── sentiment_test.py
├── similarity    #########################近义词，同义词，句子相似性
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; ├── snowNlp
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; └── sentence_similarity.py
│&nbsp;&nbsp; └── Word2vec
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     ├── sentences
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── lsi_corpus.mm
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── lsi_corpus.mm.index
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── lsi_similarity.sim
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── model.lsi
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── model.lsi.projection
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── mydict.dict
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── sentences_similer.py
│&nbsp;&nbsp;     │&nbsp;&nbsp; ├── train_corpus.txt
│&nbsp;&nbsp;     │&nbsp;&nbsp; └── train.py
│&nbsp;&nbsp;     └── words
│&nbsp;&nbsp;         ├── chinesewords.txt
│&nbsp;&nbsp;         ├── corpus.txt
│&nbsp;&nbsp;         ├── create_vec.py
│&nbsp;&nbsp;         ├── __init__.py
│&nbsp;&nbsp;         ├── plot.py
│&nbsp;&nbsp;         ├── readMe.txt
│&nbsp;&nbsp;         ├── read_vec.py
│&nbsp;&nbsp;         ├── remove_stopwords.py
│&nbsp;&nbsp;         ├── stopdict.txt
│&nbsp;&nbsp;         ├── wordvec_c.model
│&nbsp;&nbsp;         └── wordvec.model
├── text_classifier  ################聚类，监督，无监督
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── nltk
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── example.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; └── readMe.txt
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; ├── sklearn
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── data_baoxian.json
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── data.json
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── example_1.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── example_2.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── stop_baoxian.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── stopword.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; └── test.py
│&nbsp;&nbsp; └── textblob
│&nbsp;&nbsp;     ├── female.txt
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     ├── male.txt
│&nbsp;&nbsp;     ├── readMe.txt
│&nbsp;&nbsp;     ├── test2.py
│&nbsp;&nbsp;     └── test3.py
├── word_tagging   #################词性标注
│&nbsp;&nbsp; ├── crf
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── 199801.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── create_curpus.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── crf_model_1
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── curpus.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── doc.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; │&nbsp;&nbsp; └── train_and_test.py
│&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; ├── jieba
│&nbsp;&nbsp; │&nbsp;&nbsp; ├── __init__.py
│&nbsp;&nbsp; │&nbsp;&nbsp; └── word_tagging.py
│&nbsp;&nbsp; ├── readMe.txt
│&nbsp;&nbsp; └── snowNlp
│&nbsp;&nbsp;     ├── __init__.py
│&nbsp;&nbsp;     └── test.py
└── word_vector  ######################词向量提取
    ├── __init__.py
    ├── readMe.txt
    └── Word2vec
        ├── chinesewords.txt
        ├── corpus.txt
        ├── create_vec.py
        ├── __init__.py
        ├── read_vec.py
        ├── remove_stopwords.py
        ├── stopdict.txt
        ├── wordvec_c.model
        └── wordvec.model</pre>
<br />


