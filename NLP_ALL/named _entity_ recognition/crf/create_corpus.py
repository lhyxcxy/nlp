# -*- coding: utf-8 -*-
import codecs

wordfile=codecs.open("199801.txt",encoding="gbk")
curpusfile=codecs.open("corpus.txt",'w', 'utf-8')

def max_word():#最长匹配  提取[中央/n  人民/n  广播/vn  电台/n]nt  样式的词，最长词，如 :中央人民广播电台/n
    for sentence in wordfile.readlines():
        words= sentence.strip().split(" ")
        b_flag = 0
        b_word=""
        for word in words:  #提取[中央/n  人民/n  广播/vn  电台/n]nt  样式的词，最长词，如 :中央人民广播电台/n
            if word.strip()!="":
                b_tag=""
                if word.startswith("["):
                    b_flag=1
                    word=word[1:]
                elif "]" in word:
                    b_flag=2
                    b_tag = word[word.index("]") + 1:]
                    word=word[0:word.index("]")]
                w_c=word.split("/")
                if b_flag==1:
                    b_word=b_word+w_c[0];
                elif b_flag==2:
                    b_word = b_word + w_c[0];
                    b_flag=0
                    curpusfile.write(b_word + "  " + b_tag + "\n")
                    b_word = ""
                else:
                    curpusfile.write(w_c[0]+"  "+w_c[1]+"\n")



def min_word():#最短匹配   提取[中央/n  人民/n  广播/vn  电台/n]nt  样式的词，最短词，如 :中央，人民，广播，电台
    for sentence in wordfile.readlines():
        words = sentence.strip().split(" ")
        for word in words:
            if word.strip() != "":
                if word.startswith("["):
                    word = word[1:]
                elif "]" in word:
                    word = word[0:word.index("]")]
                w_c = word.split("/")
                curpusfile.write(w_c[0] + "  " + w_c[1] + "\n")