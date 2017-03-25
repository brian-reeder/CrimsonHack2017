
# calculate
def calculatePercent(): #need to take in "article" and "articleToCompair"
    print(50)

# This fuction will compair every article to eachother and determine which articles are similar to eachother
def compairArticles(array1, array2):
    for article in array1:
        for articleToCompair in array2:
            percentSimilar = calculatePercent(article, articleToCompair)
            if percentSimilar >= thresholdPercent:
                array1(article) #need to add articleToCompare to article.SimilarArticles
