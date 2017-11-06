# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 21:20:41 2017

@author: John
"""

path_spam = "D:\DataAnalystic\data607\Spam\small_spam"

import os,  nltk

from nltk.corpus import stopwords

#only run nltk.download() once only if not done so.
#nltk.download()

#remove stop words
#https://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python


# Open a file
dirs = os.listdir( path_spam )

# This would print all the files and directories
for file in dirs:    
   f = open(path_spam + "\\" + file,'r')
   raw = f.read()
   f.close()
   tokens = nltk.tokenize.word_tokenize(raw)
   
   fdist= nltk.FreqDist(tokens)
   print(fdist)
