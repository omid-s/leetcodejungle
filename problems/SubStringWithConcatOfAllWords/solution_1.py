"""


Word order does not matter
all words should be there exactly once

1- find the occurance of all words in one pass (hopefully)
2- check the indexes. we know all the words are of same length, so checking indexes of each word becomes a subtraction
3- we can store the indexes of each word in a hash table of lists to


"""


class Solution:

    def find_all(self, s, w):
        ret = []
        l = len(w) + 1
        for i in range(len(s)):
            if s[i:i + l] == w:
                ret.append(i)
        return ret

    def find_indexes(self, s, words):
        """
        returns  dictionary of words -> indexes
        :param s:
        :param words:
        :return:
        """
        ret = {}
        for w in words:
            temp = self.find_all(s, w)
            if len(temp) > 0:
                ret[w] = temp

        return ret

    def findSubstring(self, s: str, words):

        # find all the word combos :
        word_index_dict = self.find_indexes(s, words)

        if len(word_index_dict) < len(words):
            return []

        # find combinations of the words
        for


        return []
