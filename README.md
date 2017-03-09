# lhy-nlp
各种nlp 工具的使用包括 word2vec nltk textblob crf++ 等

（1）机器人
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
│   ├── __init__.py
│   └── readMe.txt
├── chinese_trans ################ 中文翻译，及繁体转简体
│   ├── __init__.py
│   ├── readMe.txt
│   └── snowNlp
│       ├── chinese_to_fanti.py
│       ├── chinese_to_pinyin.py
│       ├── __init__.py
│       └── readMe.txt
├── keywords_summary_topic  ###########关键词提取，主题提取，摘要提取
│   ├── __init__.py
│   ├── jieba
│   │   ├── __init__.py
│   │   └── keywords.py
│   ├── readMe.txt
│   ├── snowNlp
│   │   ├── __init__.py
│   │   └── keyword_summary.py
│   └── Word2vec
│       ├── deerwester.dict
│       ├── deerwester.mm
│       ├── deerwester.mm.index
│       ├── example.py
│       ├── foo.tfidf_model
│       ├── __init__.py
│       ├── lda_corpus.mm
│       ├── lda_corpus.mm.index
│       ├── lsi_corpus.mm
│       ├── lsi_corpus.mm.index
│       ├── model.lda
│       ├── model.lda.expElogbeta.npy
│       ├── model.lda.id2word
│       ├── model.lda.state
│       ├── model.lsi
│       ├── model.lsi.projection
│       ├── text1.txt
│       ├── text2.txt
│       └── text3.txt
├── named\ _entity_\ recognition #################命名体识别
│   ├── crf
│   │   ├── 199801.txt
│   │   ├── create_corpus.py
│   │   ├── crf_model_1
│   │   ├── curpus.txt
│   │   ├── doc.py
│   │   ├── __init__.py
│   │   ├── readMe.txt
│   │   └── train_and_test.py
│   ├── __init__.py
│   └── readMe.txt
├── participle       ########################分词
│   ├── crf
│   │   ├── 199801.txt
│   │   ├── crf_model
│   │   ├── crf_model_1
│   │   ├── __init__.py
│   │   ├── readMe.txt
│   │   ├── setp_1.py
│   │   ├── setp_2.py
│   │   ├── test_input.txt
│   │   ├── test_output.txt
│   │   └── train.data
│   ├── __init__.py
│   ├── jieba
│   │   ├── fenci.py
│   │   ├── __init__.py
│   │   ├── stopdict.txt
│   │   └── userdict.txt
│   ├── readMe.txt
│   └── snowNlp
│       ├── __init__.py
│       └── words_sentences.py
├── sentiment_analysis ###########################情感分析，正负类分析
│   ├── __init__.py
│   ├── readMe.txt
│   └── snowNlp
│       ├── __init__.py
│       └── sentiment_test.py
├── similarity    #########################近义词，同义词，句子相似性
│   ├── __init__.py
│   ├── readMe.txt
│   ├── snowNlp
│   │   ├── __init__.py
│   │   └── sentence_similarity.py
│   └── Word2vec
│       ├── __init__.py
│       ├── sentences
│       │   ├── __init__.py
│       │   ├── lsi_corpus.mm
│       │   ├── lsi_corpus.mm.index
│       │   ├── lsi_similarity.sim
│       │   ├── model.lsi
│       │   ├── model.lsi.projection
│       │   ├── mydict.dict
│       │   ├── readMe.txt
│       │   ├── sentences_similer.py
│       │   ├── train_corpus.txt
│       │   └── train.py
│       └── words
│           ├── chinesewords.txt
│           ├── corpus.txt
│           ├── create_vec.py
│           ├── __init__.py
│           ├── plot.py
│           ├── readMe.txt
│           ├── read_vec.py
│           ├── remove_stopwords.py
│           ├── stopdict.txt
│           ├── wordvec_c.model
│           └── wordvec.model
├── text_classifier  ################聚类，监督，无监督
│   ├── __init__.py
│   ├── nltk
│   │   ├── example.py
│   │   ├── __init__.py
│   │   └── readMe.txt
│   ├── readMe.txt
│   ├── sklearn
│   │   ├── data_baoxian.json
│   │   ├── data.json
│   │   ├── example_1.py
│   │   ├── example_2.py
│   │   ├── __init__.py
│   │   ├── readMe.txt
│   │   ├── stop_baoxian.txt
│   │   ├── stopword.txt
│   │   └── test.py
│   └── textblob
│       ├── female.txt
│       ├── __init__.py
│       ├── male.txt
│       ├── readMe.txt
│       ├── test2.py
│       └── test3.py
├── word_tagging   #################词性标注
│   ├── crf
│   │   ├── 199801.txt
│   │   ├── create_curpus.py
│   │   ├── crf_model_1
│   │   ├── curpus.txt
│   │   ├── doc.py
│   │   ├── __init__.py
│   │   ├── readMe.txt
│   │   └── train_and_test.py
│   ├── __init__.py
│   ├── jieba
│   │   ├── __init__.py
│   │   └── word_tagging.py
│   ├── readMe.txt
│   └── snowNlp
│       ├── __init__.py
│       └── test.py
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
        └── wordvec.model

