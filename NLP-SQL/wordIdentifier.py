import nltk
def wordIdentifier(query):
	
	#fucntion of nltk package which tokenizes sentences into words
	tokens=nltk.word_tokenize(query)
	print(tokens)

	#tags tokens with associatd figure of speech(like CD,VB,NN etc)
	tagged=nltk.pos_tag(tokens)
	print(tagged)
	keywords=[]
	numerals=[]
	tags = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ']
	for i in tagged:
		if i[1] in tags:
			keywords.append(i[0])
		elif i[1] == 'CD':
			numerals.append(i[0])
	return tokens,keywords,tagged,numerals
	
