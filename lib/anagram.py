# your code goes here!

input_list = []
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        anagram = []  
        #iterate over each word in the input list
        for input_word in input_list:
            # check if sorted words match
            if sorted(self.word) == sorted(input_word):
                anagram.append(input_word)
        return anagram




#sorted in python returns a sorted list of the specified iterable object. https://www.w3schools.com/python/ref_func_sorted.asp