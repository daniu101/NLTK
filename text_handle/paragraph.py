#!/usr/bin/env python
# -*- coding: utf-8

import nltk
from nltk.tokenize import sent_tokenize

# 文本切分为句子
stringtext = 'Hello.I am python. everybody good. everybody is good!'

all_sent = sent_tokenize(stringtext)
 
print(all_sent)
print(all_sent[0])
print(all_sent[1])
print(all_sent[2])

