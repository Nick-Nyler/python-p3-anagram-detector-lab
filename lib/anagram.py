# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word) 

    def match(self, possible_anagrams):
        anagrams = []
        for candidate in possible_anagrams:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word and sorted(candidate_lower) == self.sorted_word:
                anagrams.append(candidate)
        return anagrams