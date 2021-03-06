from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return randint(0,len(review_options))

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inverseIndex={}
    for i,sentence in enumerate(strlist):
        for word in sentence.split():
            inverseIndex[word]=set()
 
    for key,value in inverseIndex.items():
        for i,sentence in enumerate(strlist):
            for word in sentence.split():
                if key==word:
                    inverseIndex[word].add(i)
    return inverseIndex

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    result=set()
    for word in query:
        i=inverseIndex.get(word)
        for v in i:
            result.add(v)
    return result

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    temp=[]
    for word in query:
        i=inverseIndex.get(word)
        temp.append(i)
    return set.intersection(*temp)
