#!/usr/bin/env python
# -*- coding: utf-8

import nltk

# 输入自己 word.txt 的地址
DIR_WORD = "D:/word.txt"

text = open(DIR_WORD).read()

print(len(text)) # 文本长度
print(len(set(text)))  # 不同词个数
print(len(text[0])) # text第1个词的长度
print(len(text[1])) # text第2个词的长度

