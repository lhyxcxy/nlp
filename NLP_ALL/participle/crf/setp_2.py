#!/usr/bin/env python
# -*- coding: utf-8 -*-
# crf_segmenter.py
# 用法：命令行输入--python crf_segmenter.py crf_model input_file output_file
# 利用CRF自带的python工具包，对输入文本进行分词

import codecs
import sys

import CRFPP


def crf_segmenter(input_file, output_file, tagger):
    """
    输入文件分词
    :param input_file:
    :param output_file:
    :param tagger:
    :return:
    """
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for line in input_data.readlines():
        tagger.clear()
        for word in line.strip():
            word = word.strip()
            if word:
                tagger.add((word + "\to\tB").encode('utf-8'))
        tagger.parse()
        size = tagger.size()
        xsize = tagger.xsize()
        for i in range(0, size):
            for j in range(0, xsize):
                char = tagger.x(i, j).decode('utf-8')
                tag = tagger.y2(i)
                if tag == 'B':
                    output_data.write(' ' + char)
                elif tag == 'M':
                    output_data.write(char)
                elif tag == 'E':
                    output_data.write(char + ' ')
                else:  # tag == 'S'
                    output_data.write(' ' + char + ' ')
        output_data.write('\n')
    input_data.close()
    output_data.close()


def crf_fenci_text(input_text, tagger):
    """
    输入文本分词
    :param input_text:
    :param tagger:
    :return:
    """

    out_words_list=list();
    tagger.clear()
    for word in input_text.strip():
        word = word.strip()
        if word:
            tagger.add((word).encode('utf-8'))
    tagger.parse()
    size = tagger.size()
    xsize = tagger.xsize()
    this_word = "";
    for i in range(0, size):
        for j in range(0, xsize):
            char = tagger.x(i, j).decode('utf-8')
            tag = tagger.y2(i)
            if tag == 'B':
                this_word=char;
                #output_data.write(' ' + char)
            elif tag == 'M':
                this_word=this_word+char
                #output_data.write(char)
            elif tag == 'E':
                this_word=this_word+char;
                out_words_list.append(this_word)
                this_word="";
                break;
                #output_data.write(char + ' ')
            else:  # tag == 'S'
                this_word=char;
                out_words_list.append(this_word)
                this_word=""
                break;
                #output_data.write(' ' + char + ' ')
    return out_words_list


tagger = CRFPP.Tagger("-m " + "crf_model")
#crf_segmenter("test_input.txt", "test_output.txt", tagger)

words_list=crf_fenci_text(u"中华人民共和国正在振兴崛起",  tagger)
print (" ".join(words_list))