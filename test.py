# -*- coding: utf-8 -*-
# encoding=utf8
import math
import sys

import nltk
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.neighbors import regression

reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import re
import csv
import collections
from scipy.stats import chisquare, stats


def isCapital(string):
    #letter = ("ğöüşİÖÜŞĞ")
    if string.find("ğ") != -1:
        string = string.replace("ğ", "g");
    if string.find("Ğ") != -1:
        string = string.replace("Ğ", "G");
    if string.find("ö") != -1:
        string = string.replace("ö", "o");
    if string.find("Ö") != -1:
        string = string.replace("ğ", "g");
    if string.find("ü") != -1:
        string = string.replace("ü", "u");
    if string.find("Ü") != -1:
        string = string.replace("Ü", "U");
    if string.find("ş") != -1:
        string = string.replace("ş", "s");
    if string.find("Ş") != -1:
        string = string.replace("Ş", "S");
    if string.find("İ") != -1:
        string = string.replace("İ", "I");
    return string;

def hasPunctuation(word):
    words = []
    checker = 0
    for x in word.split(" "):
        words.append(x)

    # çoklu kelimeler icin kelimeleri ayirdik
    for y in range(0, len(words)):
        # sadece alfabetik karakter icerirse checker 1
        if (words[y].isalpha() == False):
            checker = 1
            break

    #print("hasPunc:", checker)
    return checker

def hasEmoticon(word):
    emoticons = [':)', ':(', ';)', ':O', ':D', ':P', ':@', ':S', ':$', 'B)', ':\'(', ':*', '>:)', 'O:)', ':/', ':|',
                 ':B', ':SS', ':))', '8)', ':&', ':?', '<3', '(u)']
    checker = 0

    for i in range(0, len(emoticons)):
        if emoticons[i] in word:
            checker = 1
            break

    #print("hasEmoticon:", checker)
    return checker

def hasVowel(word):
    vowel = ("aıioöuüAEIİOÖUÜ")
    hasVowel = 0
    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in vowel:
                hasVowel = 1

    return hasVowel

def hasConsonant(word):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    hasCons=0

    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in cons:
                hasCons = 1
    return hasCons

def containNumber(tweet):
    cnt = 0
    digitLst = []
    wordLst = tweet.split(" ")
    for word in wordLst:
        if (word.isdigit()):
            digitLst.append(word)
        else:
            for i in range(len(word)):
                if(word[i].isdigit()):
                    digitLst.append(word[i])
    return len(digitLst)

def hasHashtag(tweet):
    if(tweet.find('#')>=0):
        hashtagLst =1
    else:
        hashtagLst=0

    return hashtagLst

def hasMention(tweet):

    if(tweet.find('@')>=0):
        mentionLst =1
    else:
        mentionLst=0
    return mentionLst

def hasRT(tweet):
    RTLst = 0
    if(tweet.find('RT')>=0):
        RTLst =1

    return RTLst


def hasUrl(tweet) :
    urlLst = re.findall(r'(https?://[^\s]+)', tweet)
    #print("Bu tweette %d adet url var" % len(urlLst))

    return len(urlLst);

def mostUsedWord(tweet):
    wordLst = tweet.split(" ")

    for i in range(len(wordLst)):
        if wordLst[i] in tweet:
            return wordLst[i]
        else:
            return ''


def FindNumberOfWord(tweet):
    words_tweet = tweet.split(" ")
    return len(words_tweet)

def entropy(labels1, labels2):
    freqdist = nltk.FreqDist(labels1)
    freqdist2 = nltk.FreqDist(labels2)
    print 'freqdist items:',freqdist.items()
    probs = [freqdist.freq(l) for l in freqdist, freqdist2]
    print 'probs:', probs
    return -sum(p * math.log(p,2) for p in probs)

def counting(df2,feature):
    liste =[]
    for index in range (len(df2)):
        liste.append(df2.iloc[index][feature])

    return liste


def main():
    data = {
        'Word Before': [''],
        #'WB Stem': [''],
        #'WB POS Tag': [''],
        'WB Letter': [''],
        #'WB Letter Diff Stem': [''],
        'WB Is Capital': [''],
        'WB Is All Capital': [''],
        'WB Has Punct BA': [''],
        'WB Has Emot BA': [''],
        #'WB Has Double Consonant': [''],
        #'WB Has Double Vowel': [''],
        #'WB Has Harmony': [''],
        #'WB Cons Vow Ratio': [''],
        'WB Contain Number': [''],
        'WB Has Hashtag': [''],
        'WB Has Url': [''],
        'WB Class': [''],

        'Word': [''],
        #'W Stem': [''],
        #'W POS Tag': [''],
        'W Letter': [''],
        #'W Letter Diff Stem': [''],
        'W Is Capital': [''],
        'W Is All Capital': [''],
        'W Has Punct BA': [''],
        'W Has Emot BA': [''],
        #'W Has Double Consonant': [''],
        #'W Has Double Vowel': [''],
        #'W Has Harmony': [''],
        #'W Cons Vow Ratio': [''],
        'W Contain Number': [''],
        'W Has Hashtag': [''],
        'W Has Url': [''],
        'W Class': [''],

        'Word After': [''],
        #'WA Stem': [''],
        #'WA POS Tag': [''],
        'WA Letter': [''],
        #'WA Letter Diff Stem': [''],
        'WA Is Capital': [''],
        'WA Is All Capital': [''],
        'WA Has Punct BA': [''],
        'WA Has Emot BA': [''],
        #'WA Has Double Consonant': [''],
        #'WA Has Double Vowel': [''],
        #'WA Has Harmony': [''],
        #'WA Cons Vow Ratio': [''],
        'WA Contain Number': [''],
        'WA Has Hashtag': [''],
        'WA Has Url': [''],
        'WA Class': ['']
    }

    data2 ={
        'Tweet': [''],
        'Tweet has Punct BA': [''],
        'Tweet has Emot BA': [''],
        'Tweet has Hashtag': [''],
        'Tweet has Mention': [''],
        'Tweet has Url': [''],
        'Frequently used word': [''],
        'Tweet FAV Ratio': [''],
        'Tweet RT Ratio': [''],
        'Tweet Has Location': [''],
        'Tweet Has Checkin': [''],
        'Tweet From Mobile Device': [''],
        'Length of tweet as # of words': [''],
        'Length of tweet as # of characters': [''],
    }

    rows = []
    f = open('tweet1_2304.csv', 'rt')
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    finally:
        f.close()

    counter = 1
    list = []
    for i in range(1, len(rows)):
        if (rows[i][1] == rows[i - 1][1]):
            counter += 1
        else:
            list.append(counter)
            counter = 1

    # tweets[0]="id,tweet,word,tag" , list[0]=1
    # tweets[1],list[1]=3    0,3
    # tweets[4],list[2]=6    3,9
    # tweets[10],list[3]=3   9,12
    # tweets[13],list[4]=8   12,20

    index = 1
    index2 = 0
    words = []
    taglist = []
    tweetlist=[]
    for j in range(1, len(list)):

        index += list[j]
        tweetlist.append(rows[index-1][1])
        start = index2
        index2 += list[j]
        end = index2
        for word in rows[index - 1][1].split():
            tag = []
            # list(i-1),list(i-1)+list(i)
            for i in range(start, end):
                if word == rows[i + 1][2]:
                    tag.append(rows[i + 1][3])
                else:
                    tag.append('Other')

            counter = collections.Counter(tag)
            if counter.__len__() == 1:
                # print word,'Other'
                words.append(word)
                taglist.append('Other')
            else:
                tagx = counter.items().pop(0)
                words.append(word)
                taglist.append(tagx[0])
                # print word,tagx[0]


    df = pd.DataFrame(data, index=words)
    df2=pd.DataFrame(data2, index=tweetlist)


    print('.....')
    print('XXXX XXXX')

    for j in range(df.size):

        """ Word Before """
        df.iloc[j]['Word Before'] = df.index[j - 1]
        #df.iloc[j]['WB Stem'] = 'X'
        #df.iloc[j]['WB POS Tag'] = 'X'
        df.iloc[j]['WB Letter'] = len(df.index[j - 1])
        #df.iloc[j]['WB Letter Diff Stem'] = 'X'
        df.iloc[j]['WB Is Capital'] = isCapital(df.index[j - 1]).istitle()
        df.iloc[j]['WB Is All Capital'] = df.index[j - 1].isupper()
        df.iloc[j]['WB Has Punct BA'] = hasPunctuation(df.index[j - 1])
        df.iloc[j]['WB Has Emot BA'] = hasEmoticon(df.index[j - 1])
        #df.iloc[j]['WB Has Double Consonant'] = hasConsonant(df.index[j - 1])
        #df.iloc[j]['WB Has Double Vowel'] = hasVowel(df.index[j - 1])
        #df.iloc[j]['WB Has Harmony'] = ''
        df.iloc[j]['WB Contains Number'] = containNumber(df.index[j - 1])
        df.iloc[j]['WB Has Hashtag'] = hasHashtag(df.index[j - 1])
        df.iloc[j]['WB Has Url'] = hasUrl(df.index[j - 1])
        #if (countVowels(df.index[j - 1]) > 0):
        #    df.iloc[j]['WB Cons Vow Ratio'] = countCons(df.index[j - 1]) / countVowels(df.index[j - 1])
        #else:
        #    df.iloc[j]['WB Cons Vow Ratio'] = 0
        df.iloc[j]['WB Class'] = taglist[j-1]

        """ Word """
        df.iloc[j]['Word'] = df.index[j]
        #df.iloc[j]['W Stem'] = 'X'
        #df.iloc[j]['W POS Tag'] = 'X'
        df.iloc[j]['W Letter'] = len(df.index[j])
        #df.iloc[j]['W Letter Diff Stem'] = 'X'
        df.iloc[j]['W Is Capital'] = isCapital(df.index[j]).istitle()
        df.iloc[j]['W Is All Capital'] = df.index[j].isupper()
        df.iloc[j]['W Has Punct BA'] = hasPunctuation(df.index[j])
        df.iloc[j]['W Has Emot BA'] = hasEmoticon(df.index[j])
        #df.iloc[j]['W Has Double Consonant'] = hasConsonant(df.index[j])
        #df.iloc[j]['W Has Double Vowel'] = hasVowel(df.index[j])
        #df.iloc[j]['W Has Harmony'] = ''
        df.iloc[j]['W Contains Number'] = containNumber(df.index[j])
        df.iloc[j]['W Has Hashtag'] = hasHashtag(df.index[j])
        df.iloc[j]['W Has Url'] = hasUrl( df.index[j])
        #if (countVowels(df.index[j]) > 0):
        #    df.iloc[j]['W Cons Vow Ratio'] = countCons(df.index[j]) / countVowels(df.index[j])
        #else:
        #    df.iloc[j]['W Cons Vow Ratio'] = 0
        df.iloc[j]['W Class'] = taglist[j]

        """ Word After """
        df.iloc[j]['Word After'] = df.index[j + 1]
        #df.iloc[j]['WA Stem'] = df.index[j + 1]
        #df.iloc[j]['WA POS Tag'] = 'X'
        df.iloc[j]['WA Letter'] = len(df.index[j + 1])
        #df.iloc[j]['WA Letter Diff Stem'] = len(df.index[j + 1]) - len(df.index[j + 1])
        df.iloc[j]['WA Is Capital'] = isCapital(df.index[j + 1]).istitle()
        df.iloc[j]['WA Is All Capital'] = df.index[j + 1].isupper()
        df.iloc[j]['WA Has Punct BA'] = hasPunctuation(df.index[j + 1])
        df.iloc[j]['WA Has Emot BA'] = hasEmoticon(df.index[j + 1])
        #df.iloc[j]['WA Has Double Consonant'] = hasConsonant(df.index[j + 1])
        #df.iloc[j]['WA Has Double Vowel'] = hasVowel(df.index[j + 1])
        #df.iloc[j]['WA Has Harmony'] = ''
        df.iloc[j]['WA Contains Number'] = containNumber(df.index[j + 1])
        df.iloc[j]['WA Has Hashtag'] = hasHashtag(df.index[j + 1])
        df.iloc[j]['WA Has Url'] = hasUrl(df.index[j + 1])
        #if (countVowels(df.index[j + 1]) > 0):
        #    df.iloc[j]['WA Cons Vow Ratio'] = countCons(df.index[j + 1]) / countVowels(df.index[j + 1])
        #else:
        #    df.iloc[j]['WA Cons Vow Ratio'] = 0
        df.iloc[j]['WA Class'] = taglist[j + 1]

        if (j == 6500):
            break

    for i in range(len(df2)):
        df2.iloc[i]['Tweet'] = df2.index[i]
        df2.iloc[i]['Tweet has Punct BA'] =hasPunctuation(df2.index[i])
        df2.iloc[i]['Tweet has Emot BA'] = hasEmoticon(df2.index[i])
        df2.iloc[i]['Tweet has Hashtag'] = hasHashtag(df2.index[i])
        df2.iloc[i]['Tweet has Mention'] = hasMention(df2.index[i])
        df2.iloc[i]['Tweet has Url']=hasUrl(df2.index[i])
        df2.iloc[i]['Frequently used word'] ='X'
        df2.iloc[i]['Tweet FAV Ratio'] = 'X'
        df2.iloc[i]['Tweet RT Ratio'] = hasRT(df2.index[i])
        df2.iloc[i]['Tweet Has Location'] = 'X'
        df2.iloc[i]['Tweet Has Checkin'] = 'X'
        df2.iloc[i]['Tweet From Mobile Device'] = 'X'
        df2.iloc[i]['Length of tweet as # of words'] = len(df2.index[i].split())
        df2.iloc[i]['Length of tweet as # of characters'] = len(df2.iloc[i]['Tweet'])

    #print(df2.iloc[0])

    features_tweets =['Tweet has Punct BA','Tweet has Emot BA','Tweet has Hashtag','Tweet has Mention','Tweet has Url','Tweet RT Ratio','Length of tweet as # of words','Length of tweet as # of characters']

    features = ['W Is All Capital', 'W Is Capital', 'W Letter','W Has Emot BA','W Has Hashtag', 'W Has Punct BA', 'W Has Url',
                'WA Is All Capital', 'WA Is Capital','WA Letter','WA Has Emot BA','WA Has Hashtag', 'WA Has Punct BA', 'WA Has Url',
                'WB Is All Capital', 'WB Is Capital','WB Letter','WB Has Emot BA', 'WB Has Hashtag', 'WB Has Punct BA', 'WB Has Url']

    word_class =['W Class','WA Class','WB Class']

    for j in range(len(features)):

        # Information Gain Calculation
        allcap = counting(df, features[j])
        print '\n',features[j],'\n=================\nIG:', entropy(allcap)

        #Mutual Information
        print 'MI:',sklearn.metrics.mutual_info_score(df[word_class[j/7]],df[features[j]], contingency=None);

    for x in range(len(features_tweets)):

        alltweet = counting(df2, features_tweets[x])
        print '\n',features_tweets[x],'\n=================\nIG:', entropy(alltweet)

        # Mutual Information of tweets
        print 'MI:', sklearn.metrics.mutual_info_score(df2['Tweet'], df2[features_tweets[x]], contingency=None);
    ''''''
main()