#!/usr/bin/env python
# -*- coding: utf-8 -*-
# make_crf_train_data.py
# 得到CRF++要求的格式的训练文件
# 用法：命令行--python make_crf_train_data.py input_file output_file
# 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)

import codecs
import sys


def character_tagging(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'gbk')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split("  ")
        for word in word_list:
            words = word.split("/");

            if len(words) >= 2:
                xz = words[1]
                word = words[0]
                if len(word) == 1:
                    output_data.write(word + "\t" + xz + "\tS\n")
                else:
                    output_data.write(word[0] + "\t" + xz + "\tB\n")
                    for w in word[1:len(word) - 1]:
                        output_data.write(w + "\t" + xz + "\tM\n")
                    output_data.write(word[len(word) - 1] + "\t" + xz + "\tE\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()


'''''if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "pls use: python make_crf_train_data.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_tagging(input_file, output_file)'''

character_tagging("199801.txt", "train.data")