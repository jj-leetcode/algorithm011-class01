# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        word_set = set(wordList)
        L = len(wordList[0])
        index_dict = {}
        for i in range(L):
            index_dict[i] = set([x[i] for x in wordList])

        Q = [(beginWord, 1)]
        while Q:
            word, level = Q.pop(0)
            if word == endWord:
                return level
            for i in range(L):
                for c in index_dict[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        Q.append((new_word, level+1))
                        word_set.remove(new_word)
        return 0