#encoding=utf-8
import jieba
import os
import sys

words_line="";
for wordl in open('chinesewords.txt').readlines():
    words_line=words_line+" "+wordl;

stop_list = [line.strip().decode('utf-8') for line in open('stopdict.txt').readlines()]
#seg_list=list(set(seg_list)-set(stop_list));
for stop in stop_list:
    words_line=words_line.replace(stop,"")
print words_line
open('corpus.txt',"w").writelines(words_line)

