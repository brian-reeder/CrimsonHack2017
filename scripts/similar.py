# # # # # # # # # # 
#
# Check Tense Similarity
#
# Check two words to see if they
# are 'Tense Similar' or hav the same
# root word, but used in differing 
# tenses. i.e. run and running
#
def Tense_Sim(word1,word2):
        # If words are the same
        if word1 == word2:
            return True
	# Only check tense of words greater than or equal to 3 chars
        if len(word1) >= 3 & len(word2) >= 3:
	    # if both words are mutually inclusive
            if (word1 in word2) or (word2 in word1):
                return True                         
            else:
                return False
        else:
            return False

# This function will calculate a percent similarity between two articles
# def Calculate_Percent_Similarity(article1,article2)

def pcnt_sim(article1,article2):

    words1 = [] # array of the words in article1
    words2 = [] # array of the words in article2

    # Parse words over spaces
    words1 = article1.split(" ")
    words2 = article2.split(" ")

    is_same = False
    points = 0
    percent_similar = 0.0
    threshold_percent = 30.0

    # Possible number of points between shortest string length
    # aka min number of unique words
    if len(words1) > len(words2):
        shortest_length = len(words2)
    else:
        shortest_length = len(words1)

    # Compare all words in both stories
    # Award points for each hit
    for i in words1:
        for j in words2:
            is_same = Tense_Sum(i,j)
            if is_same == True:
                points += 1

    # Calculate percentage of similarity
    percent_similar = (points / shortest_length) * 100

    return percent_similar

    # if similar enough, pass
#    if percent_similar >= threshold_percent:
#        return True
    # else fail
#    else:
#        return False
