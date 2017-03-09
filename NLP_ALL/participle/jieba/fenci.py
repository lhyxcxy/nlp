#encoding=utf-8
import jieba
import os
import sys
test_text="工信处女干事每月，经过下属科室，都要亲口交代24口交换机等技术性器件的安装工作。"
#精确模式
seg_list = jieba.cut(test_text,cut_all=False)
seg_list = " ".join(seg_list)
print seg_list
#全模式
seg_list2 = jieba.cut(test_text,cut_all=True)
seg_list2 = " ".join(seg_list2)
print seg_list2
# 搜索引擎模式
seg_list3 = jieba.cut_for_search(test_text)
print(", ".join(seg_list3))

#自定义词典，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
jieba.load_userdict("userdict.txt") #动态添加词
jieba.add_word('亲口交代')
jieba.del_word('每月')#动态删除词

seg_list = jieba.cut(test_text,cut_all=False)
seg_list = " ".join(seg_list)
print seg_list

#并行分词
'''原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升
基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows
用法：'''

jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
#jieba.disable_parallel() # 关闭并行分词模式

#去除停用词
seg_gen = jieba.cut(test_text,cut_all=False)
stop_list = [line.strip().decode('utf-8') for line in open('stopdict.txt').readlines()]
#seg_list=list(set(seg_list)-set(stop_list));
seg_list=list(seg_gen)
len2=len(seg_list);
stop_set=set(stop_list);
for seg in seg_list:
    if seg in stop_set:
        seg_list.remove(seg)
len1=len(seg_list);
seg_list = " ".join(seg_list)
print seg_list

