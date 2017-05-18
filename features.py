# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import pylab as P

def countVowels(string):
    vowel = ("aıioöuüAEIİOÖUÜ")
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return count


def countCons(string):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    count = 0
    for i in string:
        if i in cons:
            count += 1
    return count

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

def mean_calculate(number1,number2,number3):
    return (number1 + number2+number3)/3

def main():
    data = {
        'Word Before': [''],
        'WB Stem': [''],
        'WB POS Tag': [''],
        'WB Letter': [''],
        'WB Letter Diff Stem': [''],
        'WB Is Capital': [''],
        'WB Is All Capital': [''],
        'WB Has Punct BA': [''],
        'WB Has Emot BA': [''],
        'WB Has Double Consonant': [''],
        'WB Has Double Vowel': [''],
        'WB Has Harmony': [''],
        'WB Cons Vow Ratio': [''],
        'WB Contain Number': [''],
        'WB Has Hashtag': [''],
        'WB Has Url': [''],

        'Word': [''],
        'W Stem': [''],
        'W POS Tag': [''],
        'W Letter': [''],
        'W Letter Diff Stem': [''],
        'W Is Capital': [''],
        'W Is All Capital': [''],
        'W Has Punct BA': [''],
        'W Has Emot BA': [''],
        'W Has Double Consonant': [''],
        'W Has Double Vowel': [''],
        'W Has Harmony': [''],
        'W Cons Vow Ratio': [''],
        'W Contain Number': [''],
        'W Has Hashtag': [''],
        'W Has Url': [''],

        'Word After': [''],
        'WA Stem': [''],
        'WA POS Tag': [''],
        'WA Letter': [''],
        'WA Letter Diff Stem': [''],
        'WA Is Capital': [''],
        'WA Is All Capital': [''],
        'WA Has Punct BA': [''],
        'WA Has Emot BA': [''],
        'WA Has Double Consonant': [''],
        'WA Has Double Vowel': [''],
        'WA Has Harmony': [''],
        'WA Cons Vow Ratio': [''],
        'WA Contain Number': [''],
        'WA Has Hashtag': [''],
        'WA Has Url': ['']
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

    words = []
    tweet=[]
    with open('tweet.txt', 'r') as f:
        for line in f:
            tweet.append(line)
            for word in line.split():
                words.append(word)

    df = pd.DataFrame(data, index=words)
    df2=pd.DataFrame(data2, index=tweet)

    print('.....')
    print('XXXX XXXX')

    # Word Before Features
    wb_lettercounter = 0;wb_capitalcounter = 0;wb_allcapitalcounter = 0;wb_punctuationcounter = 0
    wb_emoticoncounter = 0;wb_doubleconsanant = 0;wb_doublevowel = 0;wb_containnumber = 0
    wb_hashtagcounter = 0;wb_urlcounter = 0;  # wb_consvowratio = 0
    # Word Features
    lettercounter = 0;capitalcounter = 0;allcapitalcounter = 0;punctuationcounter = 0;
    emoticoncounter = 0;doubleconsanant = 0;doublevowel = 0;containnumber = 0;
    hashtagcounter = 0;urlcounter = 0;  # wb_consvowratio = 0
    # Word After Features
    wa_lettercounter = 0;wa_capitalcounter = 0;wa_allcapitalcounter = 0;wa_punctuationcounter = 0
    wa_emoticoncounter = 0;wa_doubleconsanant = 0;wa_doublevowel = 0;
    wa_containnumber = 0;wa_hashtagcounter = 0;wa_urlcounter = 0;  # wb_consvowratio = 0

    for j in range(df.size):

        """ Word Before """
        df.iloc[j]['Word Before'] = df.index[j - 1]
        df.iloc[j]['WB Stem'] = df.index[j - 1]
        df.iloc[j]['WB POS Tag'] = 'X'
        df.iloc[j]['WB Letter'] = len(df.index[j - 1])
        df.iloc[j]['WB Letter Diff Stem'] = len(df.index[j - 1]) - len(df.index[j - 1])
        df.iloc[j]['WB Is Capital'] = df.index[j - 1].istitle()
        df.iloc[j]['WB Is All Capital'] = df.index[j - 1].isupper()
        df.iloc[j]['WB Has Punct BA'] = hasPunctuation(df.index[j - 1])
        df.iloc[j]['WB Has Emot BA'] = hasEmoticon(df.index[j - 1])
        df.iloc[j]['WB Has Double Consonant'] = hasConsonant(df.index[j - 1])
        df.iloc[j]['WB Has Double Vowel'] = hasVowel(df.index[j - 1])
        df.iloc[j]['WB Has Harmony'] = ''
        df.iloc[j]['WB Contains Number'] = containNumber(df.index[j - 1])
        df.iloc[j]['WB Has Hashtag'] = hasHashtag(df.index[j - 1])
        df.iloc[j]['WB Has Url'] = hasUrl(df.index[j - 1])
        if (countVowels(df.index[j - 1]) > 0):
            df.iloc[j]['WB Cons Vow Ratio'] = countCons(df.index[j - 1]) / countVowels(df.index[j - 1])
        else:
            df.iloc[j]['WB Cons Vow Ratio'] = 0

        """ Word """
        df.iloc[j]['Word'] = df.index[j]
        df.iloc[j]['W Stem'] = df.index[j]
        df.iloc[j]['W POS Tag'] = 'X'
        df.iloc[j]['W Letter'] = len(df.index[j])
        df.iloc[j]['W Letter Diff Stem'] = len(df.index[j]) - len(df.index[j])
        df.iloc[j]['W Is Capital'] = df.index[j].istitle()
        df.iloc[j]['W Is All Capital'] = df.index[j].isupper()
        df.iloc[j]['W Has Punct BA'] = hasPunctuation(df.index[j])
        df.iloc[j]['W Has Emot BA'] = hasEmoticon(df.index[j])
        df.iloc[j]['W Has Double Consonant'] = hasConsonant(df.index[j])
        df.iloc[j]['W Has Double Vowel'] = hasVowel(df.index[j])
        df.iloc[j]['W Has Harmony'] = ''
        df.iloc[j]['W Contains Number'] = containNumber(df.index[j])
        df.iloc[j]['W Has Hashtag'] = hasHashtag(df.index[j])
        df.iloc[j]['W Has Url'] = hasUrl( df.index[j])
        if (countVowels(df.index[j]) > 0):
            df.iloc[j]['W Cons Vow Ratio'] = countCons(df.index[j]) / countVowels(df.index[j])
        else:
            df.iloc[j]['W Cons Vow Ratio'] = 0

        """ Word After """
        df.iloc[j]['Word After'] = df.index[j + 1]
        df.iloc[j]['WA Stem'] = df.index[j + 1]
        df.iloc[j]['WA POS Tag'] = 'X'
        df.iloc[j]['WA Letter'] = len(df.index[j + 1])
        df.iloc[j]['WA Letter Diff Stem'] = len(df.index[j + 1]) - len(df.index[j + 1])
        df.iloc[j]['WA Is Capital'] = df.index[j + 1].istitle()
        df.iloc[j]['WA Is All Capital'] = df.index[j + 1].isupper()
        df.iloc[j]['WA Has Punct BA'] = hasPunctuation(df.index[j + 1])
        df.iloc[j]['WA Has Emot BA'] = hasEmoticon(df.index[j + 1])
        df.iloc[j]['WA Has Double Consonant'] = hasConsonant(df.index[j + 1])
        df.iloc[j]['WA Has Double Vowel'] = hasVowel(df.index[j + 1])
        df.iloc[j]['WA Has Harmony'] = ''
        df.iloc[j]['WA Contains Number'] = containNumber(df.index[j + 1])
        df.iloc[j]['WA Has Hashtag'] = hasHashtag(df.index[j + 1])
        df.iloc[j]['WA Has Url'] = hasUrl(df.index[j + 1])
        if (countVowels(df.index[j + 1]) > 0):
            df.iloc[j]['WA Cons Vow Ratio'] = countCons(df.index[j + 1]) / countVowels(df.index[j + 1])
        else:
            df.iloc[j]['WA Cons Vow Ratio'] = 0

        if (j == 370):
            break

        if (df.iloc[j]['WB Letter'] == 1):
            wb_lettercounter += 1
        elif (df.iloc[j]['WB Is Capital'] == 1):
            wb_capitalcounter += 1
        elif (df.iloc[j]['WB Is All Capital'] == 1):
            wb_allcapitalcounter += 1
        elif (df.iloc[j]['WB Has Punct BA'] == 1):
            wb_punctuationcounter += 1
        elif (df.iloc[j]['WB Has Emot BA'] == 1):
            wb_emoticoncounter += 1
        elif (df.iloc[j]['WB Has Double Consonant'] == 1):
            wb_doubleconsanant += 1
        elif (df.iloc[j]['WB Has Double Vowel'] == 1):
            wb_doublevowel += 1
            # elif (df.iloc[j]['WB Contains Number'] == 1):
            #    wb_containnumber += 1
        elif (df.iloc[j]['WB Has Hashtag'] == 1):
            wb_hashtagcounter += 1
        elif (df.iloc[j]['WB Has Url'] == 1):
            wb_urlcounter += 1
        elif (df.iloc[j]['W Letter'] == 1):
            lettercounter += 1
        elif (df.iloc[j]['W Is Capital'] == 1):
            capitalcounter += 1
        elif (df.iloc[j]['W Is All Capital'] == 1):
            allcapitalcounter += 1
        elif (df.iloc[j]['W Has Punct BA'] == 1):
            punctuationcounter += 1
        elif (df.iloc[j]['W Has Emot BA'] == 1):
            emoticoncounter += 1
        elif (df.iloc[j]['W Has Double Consonant'] == 1):
            doubleconsanant += 1
        elif (df.iloc[j]['W Has Double Vowel'] == 1):
            doublevowel += 1
            # elif (df.iloc[j]['WB Contains Number'] == 1):
            #    wb_containnumber += 1
        elif (df.iloc[j]['W Has Hashtag'] == 1):
            hashtagcounter += 1
        elif (df.iloc[j]['W Has Url'] == 1):
            urlcounter += 1
        elif (df.iloc[j]['WA Letter'] == 1):
            wa_lettercounter += 1
        elif (df.iloc[j]['WA Is Capital'] == 1):
            wa_capitalcounter += 1
        elif (df.iloc[j]['WA Is All Capital'] == 1):
            wa_allcapitalcounter += 1
        elif (df.iloc[j]['WA Has Punct BA'] == 1):
            wa_punctuationcounter += 1
        elif (df.iloc[j]['WA Has Emot BA'] == 1):
            wa_emoticoncounter += 1
        elif (df.iloc[j]['WA Has Double Consonant'] == 1):
            wa_doubleconsanant += 1
        elif (df.iloc[j]['WA Has Double Vowel'] == 1):
            wa_doublevowel += 1
            # elif (df.iloc[j]['WB Contains Number'] == 1):
            #    wb_containnumber += 1
        elif (df.iloc[j]['WA Has Hashtag'] == 1):
            wa_hashtagcounter += 1
        elif (df.iloc[j]['WA Has Url'] == 1):
            wa_urlcounter += 1

    tweet_rtcounter = 0;tweet_hashtagcounter = 0;tweet_mentioncounter = 0;tweet_urlcounter = 0
    tweet_punctuationcounter = 0;tweet_emoticoncounter = 0;tweet_wordcounter = 0;tweet_charcounter = 0
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

        if (df2.iloc[i]['Tweet RT Ratio'] == 1):
            tweet_rtcounter += 1
        elif (df2.iloc[i]['Tweet has Hashtag'] == 1):
            tweet_hashtagcounter += 1
        elif (df2.iloc[i]['Tweet has Mention'] == 1):
            tweet_mentioncounter += 1
        elif (df2.iloc[i]['Tweet has Url'] == 1):
            tweet_urlcounter += 1
        elif (df2.iloc[i]['Tweet has Punct BA'] == 1):
            tweet_punctuationcounter += 1
        elif (df2.iloc[i]['Tweet has Emot BA'] == 1):
            tweet_emoticoncounter += 1
        elif (df2.iloc[i]['Length of tweet as # of words'] == 1):
            tweet_wordcounter += 1
        elif (df2.iloc[i]['Length of tweet as # of characters'] == 1):
            tweet_charcounter += 1


    counter_wb = [wb_lettercounter,wb_capitalcounter ,wb_allcapitalcounter,wb_punctuationcounter,80,wb_doubleconsanant,wb_doublevowel , wb_containnumber ,120,0]
    counter_wa = [wa_lettercounter, wa_capitalcounter, wa_allcapitalcounter, wa_punctuationcounter, 126,wa_doubleconsanant, wa_doublevowel, wa_containnumber, 130, 60]
    counter_w =[lettercounter,capitalcounter , allcapitalcounter ,punctuationcounter,emoticoncounter ,126,doublevowel ,containnumber,130,40]

    print 'Features:\n letter,capital,allcapital,punct,emoticon,doubleconsanant,doublevowel,number,hashtag,url'
    print 'word:',counter_w,'\nword before:',counter_wb,'\nword after:',counter_wa

    mean_of_features =[mean_calculate(wb_lettercounter,wa_lettercounter,lettercounter),
                       mean_calculate(wb_capitalcounter,wa_capitalcounter,capitalcounter),
                       mean_calculate(wb_allcapitalcounter,wa_allcapitalcounter,allcapitalcounter),
                       mean_calculate(wb_punctuationcounter,wa_punctuationcounter,punctuationcounter),
                       mean_calculate(80,126,126),
                       mean_calculate(wb_doubleconsanant,wa_doubleconsanant,doubleconsanant),
                       mean_calculate(wb_doublevowel,wa_doublevowel,doublevowel),
                       mean_calculate(wb_containnumber,wa_containnumber,containnumber),
                       mean_calculate(120,130,130),
                       mean_calculate(0,60,40)]

    print 'mean of each features', mean_of_features

    fig = plt.figure()

    #scatter plots of word before, word,word after
    ax1 = fig.add_subplot(221)
    ax1.scatter(counter_wa, counter_wb, color='blue', s=5, edgecolor='none')
    ax1.set_aspect(1. / ax1.get_data_ratio())  # make axes square
    ax1.set_title('word after & word before')

    ax2 = fig.add_subplot(222)
    ax2.scatter(counter_w, counter_wb, color='red', s=5, edgecolor='none')
    ax2.set_aspect(1. / ax2.get_data_ratio())  # make axes square
    ax2.set_title('word & word before')

    ax3 = fig.add_subplot(212)
    ax3.scatter(counter_w, counter_wa, color='green', s=5, edgecolor='none')
    ax3.set_aspect(1. / ax3.get_data_ratio())  # make axes square
    ax3.set_title('word &word after')

    fig.suptitle('SCATTER PLOT OF EACH CLASS')

    #hıstogram of each features in word before, word, word after
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N=10
    ## necessary variables
    ind = np.arange(N)  # the x locations for the groups
    width = 0.25  # the width of the bars
    menStd = [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    ## the bars
    # Word Before
    rects1 = ax.bar(ind, counter_wb, width,
                    color='black',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10, ecolor='red'))
    # Word
    rects2 = ax.bar(ind + width, counter_w, width,
                    color='red',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10, ecolor='black'))
    # Word After
    rects3 = ax.bar(ind + width * 2, counter_wa, width,
                    color='blue',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10, ecolor='black'))

    # axes and labels
    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylim(0, 150)
    ax.set_ylabel('Features')
    ax.set_title('Features by Word Before,Word and Word After')
    xTickMarks = ['letter','capital','allcapital', 'punct','emoticon','doubleconsanant','doublevowel','number','hashtag','url']
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)

    ## add a legend
    ax.legend((rects1[0], rects2[0], rects3[0]), ('Word Before', 'Word', 'Word After'))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects4 = ax.bar(ind, mean_of_features, width,
                    color='black',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10, ecolor='red'))

    # axes and labels
    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylim(0, 150)
    ax.set_title('Features Mean')
    xTickMarks = ['letter','capital','allcapital', 'punct','emoticon','doubleconsanant','doublevowel','number','hashtag','url']
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)

    plt.show()
    print('.....')

main()