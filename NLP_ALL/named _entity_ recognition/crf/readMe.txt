
(1)利用crf++的训练工具crf_learn来训练模型了，切换到CRF++0.58目录下，执行如下命令即可：
    crf_learn -f 3 -c 1.5 ./example/seg/template ../curpus.txt  crf_model_1
(2)使用crf_model_1 进行命名体识别