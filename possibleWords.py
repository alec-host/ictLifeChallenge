#!/usr/bin/python
"""
 {Name}:{possible Words}
 {Author}:{alex}
"""
import time
import queue
import urllib.request as ur

from itertools import permutations

"""
-.routine to download words.
"""
def downloadEnglishDictionary():
    try:
        q = queue.Queue()

        url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
        data = ur.urlopen(url)
        myfile = data.read().decode('utf-8')

        q.put(myfile.splitlines())

        wordSet = q.get()

    except Exception as e:
        print(str(e))
        wordSet = ""

    return wordSet


"""
-.routine to search for matching words based on the subsets of our input.
"""
def getEnglishWord(inputWords, dictionaryWords):
    generatedSubsetCharacter = []

    for i in range(0, len(inputWords)+1):
        """
        -.generate subset.
        -.am using keyword set ensure that our input has unique characters b4 running permutations.
        -.duplicate characters in our input will result into permutations that will for a long period (infinite).
        """
        for item in permutations(list(set(inputWords)), i):
            generatedSubsetCharacter.append(''.join(item))

    # print(generatedSubsetCharacter)
    """
	-.return matching words based on the dictionaryWords.
	"""
    for matchingWord in (list(set(generatedSubsetCharacter) & set(dictionaryWords))):
        """
        -.display result to console.
        """
        print(matchingWord)


if __name__ == "__main__":
    """
    -.input list
    """
    inputWordList = ["cat", "dog", "museum", "photosynthesis", "typewriter"]
    """
	-.get start time b4 download.
	"""
    download_start_time = time.time()
    """
	-.routine call to initiate download.
	"""
    dictionaryWords = downloadEnglishDictionary()
    """
	-display end time for dictionary download.
	"""
    print("-- Dictionary word download completed in %s seconds " %
          (time.time() - download_start_time))
    """
	-.get start time b4 search.
	"""
    start_time = time.time()
    """
	-.routine call to initiate search.
	"""
    for j in range(0, len(inputWordList)):
        getEnglishWord(inputWordList[j], dictionaryWords)
    """
	-display end time for search.
	"""
    print("-- Search completed in %s seconds " % (time.time() - start_time))
