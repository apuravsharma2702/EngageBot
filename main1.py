import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle
import os.path
import csv
with open("intents3.json",encoding="utf-8-sig") as file:
    data = json.load(file, strict = False)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)
tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if os.path.exists(r"model.tflearn.index"):
    model.load("model.tflearn")
else:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")
    

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def split_query(txt,seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

def saveData(inputQuery,tag):
    listobj=[]
    listobj.append(inputQuery)
    listobj.append(tag)
    print(listobj)
    f=None
    try:
        with open('update.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(listobj)
    except Exception as e:
        print("issue",e)
    finally:
        if f is not None:
            f.close()
            
def chat(usrText):
    inp=usrText.strip()
    sep=(",","and",";",":","also","or","/")
    x=split_query(inp,sep)
    c=['I dont understand,Try another Question', 'Sorry, Answer not found', 'Sorry, Not getting your question']
    l=[]
    for j in x:
        results = model.predict([bag_of_words(j, words)])
        print(results)
        for i in results:
            results = i
        #print(results)
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        print(tag)
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    l.append(responses[0])
            #print(l)
        else:
            l.append(c[0])
            saveData(inp,tag)
    return(l)
