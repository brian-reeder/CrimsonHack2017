article1 = 'dog poop trump great again'
article2 = 'cat poop trump'
testbool = False

# this function figures out if the words being compared are the same word, but different tenses
# return true is the words are the same, false if they are different
def Tense_Sum(word1,word2): # takes in 2 words
        if word1 == word2:  # if the words are the same, they are indeed the same 
            return True
        if len(word1) >= 3 & len(word2) >= 3:       # if the length of both the words are >= 3
            if word1 in word2 or word2 in word1:    # if word1 is in word2 or word2 is in word1
                return True                         # if the above 2 conditions are true, return true, else return false
            else:
                return False
        else:
            return False

# This function will calculate a percent similarity between two articles
# def Calculate_Percent_Similarity(article1,article2)
def Are_Similar(article1,article2):

    words1 = []                         # array of the words in article1
    words2 = []                         # array of the words in article2

    words1 = article1.split(" ")        # actually splits the words in article1 and assigns it to the array words1
    words2 = article2.split(" ")        # actually splits the words in article2 and assigns it to the array words2

    is_same = False                     # bool that holds whether or not the two words are the same
    points = 0                          # the number of word matches found between the articles
    percent_similar = 0                 # the percent similarity between the articles.
    threshold_percent = 30              # the minimum percent similarity required to be considered similar

    if len(words1) > len(words2):       # find which article has less words, used to calculate percent_similar
        shortest_length = len(words2)   # assign shortest_length to the number of words in article 2
    else:
        shortest_length = len(words1)   # assign shortest_length to the number of words in article 1

    # The for loops below compares all the words to eachother and adds a point if they are the same word
    for i in words1:
        for j in words2:
            is_same = Tense_Sum(i,j)
            if is_same == True:
                points += 1

    points *= 100                       # multiply points by 100 to help calculate percent_similar
    percent_similar = points / shortest_length

    # if the percentage of similar words is greater then the threshold percentage, return true. else false
    if percent_similar >= threshold_percent:
        return True
    else:
        return False
testbool = Are_Similar(article1,article2)
print testbool
