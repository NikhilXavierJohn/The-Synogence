from PIL import Image
import urllib.request
import datetime
import collections
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import numpy as numpy
import re
import string
import warnings
import random
import sys
from gensim.summarization import summarize

#TEXT SUMMARIZER
def theprogramlife(filename):
    myNames = []
    with open(filename, 'r') as f:
        mySames = [line.strip() for line in f]
    myNames.append(mySames)
    with open(filename,'r') as mal:
        str=''
        for i in mal:
            str=str+i

        stopWords = set(stopwords.words("english"))
        words = word_tokenize(str)
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        #print(freqTable)
        sentences = sent_tokenize(str)
        #print(sentences)
        #5print(sentences)
        sentenceValue = dict()

        for sentence in sentences:
            #print(sentence)
            for wordValue in freqTable:
                if wordValue in sentence.lower():
                    #print(wordValue[1])
                    if sentence in sentenceValue:
                        #print(sentence)
                        sentenceValue[sentence] += 1
                        #print(sentenceValue)
                    else:
                        sentenceValue[sentence] = 1
        #print(sentenceValue)
        sumValues = 0
        #print(sentenceValue)
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        average = int(sumValues/ len(sentenceValue))
        summary = ''
        for sentence in sentences:
                if sentence in sentenceValue and sentenceValue[sentence] > (0.8*average):
                    summary +=  " " + sentence
        print(summary)
        file=open("summary.txt","w")
        file.write(summary)
        file.close()
        mywars = []
        mywars.append(summary)
        myNames.append(mywars)
    sumtext = summary



    #TO DISPLAY FREQUENT WORDS

    # Read input file, note the encoding is specified here 
    # It may be different in your text file
    file = open(filename, encoding="utf8")
    a= file.read()
    stopwordes = set(line.strip() for line in open('stopwords.txt'))
    stopwordes = stopwordes.union(set(['mr','mrs','one','two','said']))
    wordcount = {}
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in stopwordes:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    # Print most common word
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    # f = open('/home/pruce/Documents/my_stone_profile-web_Free19-03-2018_1758074546/web/output2.js', 'w')
    # f.write('var b = '+ '"' + 'The most common words are ')
    myworld =[]
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
        # f.write(word + " ")
        myworld.append(word)
    # Close the file
    # f.write('";')
    # f.close()
    file.close()
    # Create a data frame of the most common words 
    # Draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')

    myNames.append(myworld)



    #PREDICTION OF THE TEXT
    warnings.simplefilter('ignore',DeprecationWarning)
    dataset = pd.read_csv("thanks.csv")
    def clean_text(s):
            s = s.lower()
            for ch in string.punctuation:                                                                                                     
                s = s.replace(ch, " ") 
            s = re.sub("[0-9]+", "||DIG||",s)
            s = re.sub(' +',' ', s)        
            return s

    dataset['TEXT'] = [clean_text(s) for s in dataset['TITLE']]


    # pull the data into vectors
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(dataset['TEXT'])

    encoder = LabelEncoder()
    y = encoder.fit_transform(dataset['CATEGORY'])

    # split into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # take a look at the shape of each of these
    # print(x_train.shape)
    # print(y_train.shape)
    # print(x_test.shape)
    # print(y_test.shape)

    nb = MultinomialNB()
    nb.fit(x_train, y_train)
    results_nb_cv = cross_val_score(nb, x_train, y_train, cv=10)
    #print(results_nb_cv.mean())
    nb.score(x_test, y_test)
    x_test_pred = nb.predict(x_test)
    confusion_matrix(y_test, x_test_pred)
    #print(classification_report(y_test, x_test_pred, target_names=encoder.classes_))
    results_nb_cv = cross_val_score(nb, x_train, y_train, cv=10)
    # print(str(results_nb_cv.mean()*100)+"%")
    def predict_cat(title):
        cat_names = {'b' : 'business', 't' : 'science and technology', 'et' : 'entertainment', 'm' : 'health', 'w' : 'weather', 'ed' : 'education', 'c' : 'crime', 'sp' : 'sports'}
        cod = nb.predict(vectorizer.transform([title]))
        return cat_names[encoder.inverse_transform(cod)[0]]
    myPred = []
    #importing the given summary to the dataset(learns)

    def fetchandget(summary):
        category=predict_cat(summary)
        print(category)
        catfile=open("fakenews.txt","w")
        catfile.write(category)
        catfile.close()
        myPred.append(category)
        import csv
        if(category=="business"):
                category="b"
        elif(category=="science and technology"):
            category="t"
        elif(category=="entertainment"):
            category="et"
        elif(category=="health"):
            category="m"
        elif(category=="weather"):
            category="w"
        elif(category=="education"):
            category="ed"
        elif(category=="crime"):
            category="c"
        elif(category=="sports"):
            category="sp"
    fetchandget(sumtext)
    myNames.append(myPred)

theprogramlife('transcript.txt')

