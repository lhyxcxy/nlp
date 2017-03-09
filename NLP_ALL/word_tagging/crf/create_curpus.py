# -*- coding: utf-8 -*-
import codecs

wordfile=codecs.open("199801.txt",encoding="gbk")
curpusfile=codecs.open("curpus.txt",'w', 'utf-8')

for sentence in wordfile.readlines():
    words= sentence.strip().split(" ")
    for word in words:
        if word.strip()!="":
            w_c=word.split("/")
            curpusfile.write(w_c[0]+"  "+w_c[1]+"\n")


