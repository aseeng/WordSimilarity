from nltk.corpus import wordnet as wn
import math
import numpy as np


def similarity(syn1,syn2):

    commonAncestor = syn1.lowest_common_hypernyms(syn2)
    depthLCS = commonAncestor[0].max_depth()

    depth1 = syn1.max_depth()
    depth2 = syn2.max_depth()

    length = depth1 + depth2 - 2 * depthLCS
    DEPTH_MAX = 18
    value = []

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
