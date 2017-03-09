(1)为了得到适合拿来训练的数据集（4-tag标记），
    词首，常用B表示
    词中，常用M表示
    词尾，常用E表示
    单子词，常用S表示

    需要先把人民日报语料199801.txt，转成4-tag 的train.data

(2)有了训练语料，接下来就可以利用crf的训练工具crf_learn来训练模型了，切换到CRF++0.58目录下，执行如下命令即可：
    crf_learn -f 3 -c 1.5 ./example/seg/template ../tag4OutputFilePath  crf_model
(3)
进行分词