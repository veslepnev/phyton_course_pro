def filter_anagrams(word, anagrams):
    return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]