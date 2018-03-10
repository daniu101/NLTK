#!/usr/bin/env python
# -*- coding: utf-8

import nltk
from nltk.tokenize import word_tokenize

# 把句子切分为单词
stringtext = 'everyone is ok!'
 
all_word = word_tokenize(stringtext)
 
print(all_word)

