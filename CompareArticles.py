
# calculate how similar the two articles are
def calculatePercent(): #need to take in "article" and "articleToCompare"
    print(50)

# This fuction will compare every article to eachother and determine which articles are similar to eachother
def compareArticles(array1, array2):
    for article in array1:
        for articleToCompare in array2:
            percentSimilar = calculatePercent(article, articleToCompare)
            if percentSimilar >= thresholdPercent:
                array1(article) #need to add articleToCompare to article.SimilarArticles
