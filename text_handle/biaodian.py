#!/usr/bin/env python
# -*- coding: utf-8

import nltk  
  
#去标点  
text = "Hello. I am python. everybody good.everybody is good!".lower()  
print(text)
text_list = nltk.word_tokenize(text)  
#去掉标点符号  
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']  
text_list2 = [word for word in text_list if word not in english_punctuations]  
print(text_list2)
