# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 22:18:53 2017
Data 607 Project 4 spam detection
This is second file which will determine the files are spam or ham
Note that:  
From my observation, the better formula to determin the files spam or ham
    The file is span if (sum of spam_score / sum of ham_score) > 0.15
    Meaning, if 15% of the words in the file contains spam words, it is probably a spam file

    Spam_Ham_Threshold = 0.15   

After determinig spam or ham, files will be move to separated folder for accuracy check

"spam_ham_.csv" report will be created in path_report for reviewing spam_ham_ratio

Test:
 Raw data:   "http://spamassassin.apache.org/old/publiccorpus/"
 Build spam and ham frequency information from 20021010  
     spam (501 files)
     ham (2551 files)

 Unknown file Testing from 20030228
 Files are renamed with pre-fix "spam", "hard_ham", "easy_ham" to ensure the file source.
 But the program only judge the file with content.
     spam 500
     hard_ham 250
     easy_ham 2500

 
 Results:
  1.   2703 files are found In Ham folder:
      52 are actually spam
      
  2.   547 files are found in Spam folder:
      99 files are hard_ham
      0 files is easy_ham




@author: John
"""
import os,  nltk
import string


import csv

#raw spam and ham frequency files
path_score = "D:\DataAnalystic\data607\Spam"

#path to save the result
path_report = "D:\DataAnalystic\data607\Spam"

#path for unknown files
path_unknown = "D:\DataAnalystic\data607\Spam\unknown"

#path where the spam file will be moved to (from unknown)
path_is_spam = "D:\DataAnalystic\data607\Spam\is_spam"

#path where the ham file will be moved to (from unknown) 
path_is_ham = "D:\DataAnalystic\data607\Spam\is_ham"

Spam_Ham_Threshold = 0.15

##########read spam and ham freq
tokens_spam ={}
tokens_ham = {}
 
csvfile_spam = open(path_score +  "\\spam_freq.csv")
csvReader_spam = csv.reader(csvfile_spam, delimiter = ',')
 
for row in csvReader_spam:
    tokens_spam[row[0]] = int(row[1])


csvfile_ham = open(path_score +  "\\ham_freq.csv")
csvReader_ham = csv.reader(csvfile_ham, delimiter = ',')
 
for row in csvReader_ham:
    tokens_ham[row[0]] = int(row[1])

##########

#load filename for files in unknown folder
dirs_unknown = os.listdir( path_unknown )



#output spam and ham report
ofile_spam_ham_report = open( path_report + "\\spam_ham_.csv", 'wb')
ofile_spam_ham_report.write("Spam_Ham_Ratio,Spam,Ham,Filename")





#this file use the result from spam list and decide is the current files are spend or not
for file in dirs_unknown:    
    f = open(path_unknown + "\\" + file,'r')
    raw = f.read()
    f.close()
    #get bag of words
    no_punctuation = raw.lower().translate(None, string.punctuation)
    unknown_tokens = nltk.tokenize.word_tokenize(no_punctuation)
    unknown_tokens = set(unknown_tokens)
    
    unknown_tokens_spam = {}
    unknown_tokens_ham = {}
    
    #look up spam and ham frequency
    for t in unknown_tokens:
        #for get spam frequency, if unknown tokens is not found , assign zero  
        if t in tokens_spam:
            unknown_tokens_spam[t] = tokens_spam[t]
        else:
             unknown_tokens_spam[t] = 0

        #for get ham frequency, if unknown tokens is not found , assign zero  
        if t in tokens_ham:
            unknown_tokens_ham[t] = tokens_ham[t]
        else:
             unknown_tokens_ham[t] = 0
                              
    #calculate document spam and ham token weight
    # spam_score = spam_freq/(spam_freq + ham_freq)
    # ham_score = 1 - spam_score
    # avoid zero division error
    
    unknown_tokens_spam_score = {}
    unknown_tokens_ham_score = {}
    
    #calculate spam and ham score for each words
    #assign 0.0 for score if the word is new and not in both spam and ham list
    
    for t in unknown_tokens:
        if((unknown_tokens_spam[t] + unknown_tokens_ham[t]) == 0):
            unknown_tokens_spam_score[t] = 0.0
            unknown_tokens_ham_score[t] = 0.0
        else:                             
            unknown_tokens_spam_score[t] =  unknown_tokens_spam[t]/(unknown_tokens_spam[t] + unknown_tokens_ham[t] )
            unknown_tokens_ham_score[t] = 1 - unknown_tokens_spam_score[t]
     
    
    
    sum_unknown_token_spam_score = 0.0
    sum_unknown_token_ham_score = 0.0
    for t in unknown_tokens:   
        sum_unknown_token_spam_score = sum_unknown_token_spam_score + unknown_tokens_spam_score[t]
        sum_unknown_token_ham_score = sum_unknown_token_ham_score + unknown_tokens_ham_score[t]

    ###### this is the key value to determine the spam or ham 
    spam_ham_ratio = round(sum_unknown_token_spam_score/sum_unknown_token_ham_score,3)
    #####
    
    #output result to both console and file        
    print(str(spam_ham_ratio) + "," + str(sum_unknown_token_spam_score) + "," + str(sum_unknown_token_ham_score) + "," +  path_unknown + "\\" + file)    
    ofile_spam_ham_report.write(str(spam_ham_ratio) + "," + str(sum_unknown_token_spam_score) + "," + str(sum_unknown_token_ham_score) + "," +  path_unknown + "\\" + file + "\n")
    
    
    #if spam_score is higher, move the unknown file to is_spam folder, otherwise, move the fiel to is_ham folder
  
    if spam_ham_ratio > Spam_Ham_Threshold :
        os.rename(path_unknown + "\\" + file, path_is_spam + "\\" + file)
    else:
        os.rename(path_unknown + "\\" + file, path_is_ham + "\\" + file)

ofile_spam_ham_report.close()
