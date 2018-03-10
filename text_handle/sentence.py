#!/usr/bin/env python
# -*- coding: utf-8

import nltk
from nltk.tokenize import word_tokenize

# 把句子切分为单词
stringtext = 'everyone is ok!'
 
all_word = word_tokenize(stringtext)
 
print(all_word)
print(all_word[0])
print(all_word[1])
print(all_word[2])
print(all_word[3])

