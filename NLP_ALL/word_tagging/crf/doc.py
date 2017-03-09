#!/usr/bin/ruby
# -*- coding: utf-8 -*-
import CRFPP
import sys
"""
官方测试文件
"""
try:
    # -v 3: access deep information like alpha,beta,prob
    # -nN: enable nbest output. N should be >= 2
    tagger = CRFPP.Tagger("-m ./crf_model_1 -v 3 -n2")
    #tagger = CRFPP.Tagger("-m " + "crf_model_1")

    # clear internal context
    tagger.clear()

    # add context  注意 tagger.add的单词是有顺序的
    """tagger.add("Confidence NN")
    tagger.add("in IN")
    tagger.add("the DT")
    tagger.add("pound NN")
    tagger.add("is VBZ")
    tagger.add("widely RB")
    tagger.add("expected VBN")
    tagger.add("to TO")
    tagger.add("take VB")
    tagger.add("another DT")
    tagger.add("sharp JJ")
    tagger.add("dive NN")
    tagger.add("if IN")
    tagger.add("trade NN")
    tagger.add("figures NNS")
    tagger.add("for IN")
    tagger.add("September NNP")"""

    tagger.add("的".encode('utf-8'))

    print "column size: " , tagger.xsize() # 列大小
    print "token size: " , tagger.size() #tagger.add的大小
    print "tag size: " , tagger.ysize() # 标签数量
    #tagger.x(i, j) add的单词  i为
    #tagger.y(i) add单词下标对应的tag下标
    #tagger.y(i)  add单词下标对应的tag
    #tagger.yname(i) tag下标对应得tag名字
    print "tagset information:"
    ysize = tagger.ysize()
    for i in range(0, ysize-1):
        print "tag " , i , " " , tagger.yname(i)

    # parse and change internal stated as 'parsed'
    tagger.parse()

    print "conditional prob=" , tagger.prob(), " log(Z)=" , tagger.Z()

    size = tagger.size()
    xsize = tagger.xsize()
    for i in range(0, (size - 1)):
       for j in range(0, (xsize-1)):
          print tagger.x(i, j) , "\t",
       print tagger.y2(i) , "\t",
       print "Details",
       for j in range(0, (ysize-1)):
          print "\t" , tagger.yname(j) , "/prob=" , tagger.prob(i,j),"/alpha=" , tagger.alpha(i, j),"/beta=" , tagger.beta(i, j),
       print "\n",

    print "nbest outputs:"
    for n in range(0, 9):
        if (not tagger.next()):
            continue
        print "nbest n=" , n , "\tconditional prob=" , tagger.prob()
        # you can access any information using tagger.y()...

    print "Done"

except RuntimeError, e:
    print "RuntimeError: ", e,