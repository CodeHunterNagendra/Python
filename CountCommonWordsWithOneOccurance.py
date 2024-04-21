class Solution:
    def countWords(self, words1, words2) -> int:
        c = 0
        result = []
        for word1 in words1:
            for word2 in words2:
                if word1 == word2:
                    c +=1
            if c == 1:
                result.append(word1)
        return len(result)

        