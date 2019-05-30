from builtins import print

from nltk.corpus import wordnet as wn
import math
import numpy as np

def findAllHypernym(syn,hypernym):

    s = syn.hypernyms()
    ent = wn.synset('entity.n.01')
    if len(s) == 0:
        hypernym.append(syn)
        return

    if s[0] == ent:

        hypernym.append(s[0])
        return

    hypernym.append(s[0])
    findAllHypernym(s[0], hypernym)

def similarity(syn1,syn2):

    print(syn1)
    print(syn2)

    hypernym1 = []
    hypernym2 = []

    findAllHypernym(syn1, hypernym1)
    findAllHypernym(syn2, hypernym2)

    commonAncestor = ""
    depthLCS = 0

    for i in hypernym1:
        if i in hypernym2:
            commonAncestor = i
            break

    if not commonAncestor is "":
        depthLCS = commonAncestor.max_depth()

    else:
        depthLCS = -1

    depth1 = syn1.max_depth()
    depth2 = syn2.max_depth()

    value = []
    DEPTH_MAX = 18

    if not depthLCS == -1:
        length = depth1 + depth2 - 2 * depthLCS

        #Wu Palmer
        value.append(2 * depthLCS / (depth1 + depth2))

        #Shortest Path
        value.append(2 * DEPTH_MAX - length)

        #LeakcockChodorow
        value.append(math.log2((length + 1) / 2 * (DEPTH_MAX + 1)))

    return value

def findSimilarity(lemma1 , lemma2):


    synset1 = wn.synsets(lemma1,pos="n")
    synset2 = wn.synsets(lemma2,pos="n")

    maxvalue = [0,0,0]

    for syn1 in synset1:
        for syn2 in synset2:
            values = similarity(syn1,syn2)
            for v in range(len(values)):
                if values[v] > maxvalue[v]:
                    maxvalue[v] = values[v]

    return maxvalue




def rankify(array):

    newArray = []

    for i in range(len(array)):
        minori, uguali = 1, 1

        for j in range(len(array)):
            if j != i and array[j] < array[i]:
                minori += 1
            if j != i and array[j] == array[i]:
                uguali += 1

        newArray.append(minori + (uguali - 1) / 2)

    return newArray


def pearson(array, target):

    covariance = np.cov(array, target)
    standardDeviationX = np.std(array)
    standardDeviationY = np.std(target)

    return covariance / (standardDeviationX * standardDeviationY)


def spearman(array, target):

    rankTarget = rankify(array)
    rankArray = rankify(target)

    covariance = np.cov(rankArray, rankTarget)
    standardDeviationX = np.std(rankArray)
    standardDeviationY = np.std(rankTarget)

    return covariance / (standardDeviationX * standardDeviationY)
