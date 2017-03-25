article1 = 'dog poop trump great again'
article2 = 'cat poop trump'
testbool = False
# This function will calculate a percent similarity between two articles
# def Calculate_Percent_Similarity(article1,article2)
def Are_Similar(article1,article2):

    words1 = []
    words2 = []

    words1 = article1.split(" ")
    words2 = article2.split(" ")

    is_same = False
    points = 0
    percent_similar = 0
    threshold_percent = 30

    if len(words1) > len(words2):
        shortest_length = len(words2)
    else:
        shortest_length = len(words1)

    print words1
    print words2

    def Tense_Sum(word1,word2):
        if word1 == word2:
            return True
        if len(word1) >= 3 & len(word2) >= 3:
            if word1 in word2 or word2 in word1:
                print word1, word2
                return True
            else:
                return False
        else:
            return False
# The for loop below takes all the words in the articles and compares it 
    for i in words1:
        for j in words2:
            is_same = Tense_Sum(i,j)
            if is_same == True:
                points += 1

    points *= 100
    percent_similar = points / shortest_length

    if percent_similar >= threshold_percent:
        return True
    else:
        return False
testbool = Are_Similar(article1,article2)
print testbool

