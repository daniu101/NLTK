#!/usr/bin/env python
# -*- coding: utf-8

import nltk  
from nltk.tokenize import word_tokenize
  
#标出词性
text = "i love you"  
print(nltk.pos_tag(word_tokenize(text)))

# http://blog.csdn.net/zzulp/article/details/77164988
# http://blog.csdn.net/heyongluoyao8/article/details/43731743