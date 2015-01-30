
def count(text, pattern):
	'''
	returns the number of times a pattern is in text
	'''
	counter = 0
	pattern_length = len(pattern)
	for i in range((len(text) - pattern_length) + 1):
		if text[i:i + pattern_length] == pattern:
			counter += 1
	return counter


def frequent_words(text, k):
	'''
	returns the most frequently occuring k-mers in text
	'''
	#Keep track of words already seen so we aren't continously looping through the text
	#important if text is very large
	frequent_words = []
	infrequent_words = []
	#keep track of highest word frequency to determine which words are frequent
	most_occurences = 0
	for i in range((len(text) - k) + 1):
		pattern = text[i:i + k]
		#make sure we havent seen the word before. If we have, dont bother counting
		if pattern in frequent_words or pattern in infrequent_words:
			continue
		counter = count(text,pattern)
		#this pattern has the highest occurences so far
		if counter > most_occurences:
			most_occurences = counter
			#previous frequent words no longer have highest frequency, so add them to infrequent words before clearing
			infrequent_words.extend(frequent_words)
			frequent_words = []
			frequent_words.append(pattern)
		#
		elif counter == most_occurences:
			frequent_words.append(pattern)
		else:
			infrequent_words.append(pattern)
	return frequent_words

print(frequent_words('CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG',
12))

