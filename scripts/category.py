def category(Stories1, Stories2):
        relational_construct = {}
	for s1 in Stories1:
		print s1['title']
		string_s1 = s1['title'] + ' ' + s1['summary']
		relational_construct[string_s1] = []
                relational_construct[string_s1].append(str(s1))
		for s2 in Stories2:
			string_s2 = s2['title'] + ' ' + s2['summary']

#			if(pcnt_sim(string_s1, string_s2)):
			if(string_s1 == string_s2):
				print 'This is true!'
				relational_construct[string_s1].append(s2)
				Stories1.remove(s2)
				Stories2.remove(s2)
			else:
				print 'This failed!'
	return relational_construct
