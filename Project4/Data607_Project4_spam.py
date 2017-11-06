# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 21:20:41 2017
Data 607 Project 4 Spam Detection
This is the first file that create spam and ham freq (for score)
@author: Yuen Chun Wong
"""

import os,  nltk
import string


#only run nltk.download() once only if not done so.
#nltk.download()



path_spam = "D:\DataAnalystic\data607\Spam\spam"
path_ham = "D:\DataAnalystic\data607\Spam\easy_ham"

path_score = "D:\DataAnalystic\data607\Spam"




# Open a file
dirs_spam = os.listdir( path_spam )
dirs_ham = os.listdir( path_ham )


#store the frequency of words in spam and ham documents
tokens_spam = {}
tokens_ham = {}


#add detection for numtextnum or numtext format?


# This would print all the files and directories
for file in dirs_spam:    
    f = open(path_spam + "\\" + file,'r')
    raw = f.read()
    f.close()
    #get bag of words
    no_punctuation = raw.lower().translate(None, string.punctuation)
    tokens = nltk.tokenize.word_tokenize(no_punctuation)
    tokens = set(tokens)
    for t in tokens:
        if t in tokens_spam:
            tokens_spam[t] = tokens_spam[t] + 1
        else:
            tokens_spam[t] = 1


for file in dirs_ham:    
    f = open(path_ham + "\\" + file,'r')
    raw = f.read()
    f.close()
    #get bag of words
    no_punctuation = raw.lower().translate(None, string.punctuation)
    tokens = nltk.tokenize.word_tokenize(no_punctuation)
    tokens = set(tokens)
    for t in tokens:
        if t in tokens_ham:
            tokens_ham[t] = tokens_ham[t] + 1
        else:
            tokens_ham[t] = 1

 
#output spam freq
ofile_spam = open( path_score + "\\spam_freq.csv", 'wb')
for item_ts in tokens_spam:
    ofile_spam.write(item_ts + "," + str(tokens_spam[item_ts]) + "\n")
ofile_spam.close()



#output ham freq
ofile_ham = open( path_score + "\\ham_freq.csv", 'wb')
for item_ts in tokens_ham:
    ofile_ham.write(item_ts + "," + str(tokens_ham[item_ts])+ "\n")
ofile_ham.close()
    
    
    
    


