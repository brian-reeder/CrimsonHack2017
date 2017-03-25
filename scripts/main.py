from category import category 

S_1 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}]
S_2 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}]

#S_1 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}, {'title': 'Putin', 'summary': 'Putin'}]
#S_2 = [{'title': 'Trump Bombs Mexico', 'summary': 'Trump'}, {'title': 'Putin', 'summary': 'Putin'}]

new_var = category(S_1, S_2)

for n_list in new_var:
	print '----------'
	print n_list
	print
	for story in new_var[n_list]:
		print story
