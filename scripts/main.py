from category import category 

#S_1 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}]
#S_2 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}]

S_1 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}, {'title': 'Putin', 'summary': 'Putin'}, {'title': 'Trump Bombs BBC', 'summary': 'Trump'}, {'title': 'Putin Loves Snakes', 'summary': 'Putin'}]
S_2= [{'title': 'Putin', 'summary': 'Putin'}, {'title': 'Trump Bombs BBC', 'summary': 'Trump'}, {'title': 'Putin Loves Snakes', 'summary': 'Putin'}]
#S_2 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}, {'title': 'Putin', 'summary': 'Putin'}]

thresh = 30.0

new_var = category(S_1, S_2, thresh)

for n_list in new_var:
	print '----------'
	print n_list
	print
	for story in new_var[n_list]:
		print story
