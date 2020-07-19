# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        self.word_set = set(wordList)
        L = len(wordList[0])
        index_dict = {}
        ans = []
        for i in range(L):
            index_dict[i] = set([x[i] for x in wordList])

        level = [(beginWord, [beginWord])]

        def compute_current_level_and_update(layer):
            current_layer_keys = set()
            for word, path in layer:
                for i in range(L):
                    for c in index_dict[i]:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in self.word_set:
                                if new_word == endWord:
                                    ans.append(path + [new_word])
                                else:
                                    new_level.append((new_word, path + [new_word]))
                            current_layer_keys.add(new_word)
            self.word_set -= current_layer_keys

        while level:
            new_level = []
            compute_current_level_and_update(level)
            level = new_level
        return ans