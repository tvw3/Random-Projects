
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

def reverse_complement(pattern):
	'''
	returns the reverse complement of the pattern string
	'''
	#translation dictionary, includes lower and upper case for more robust input acceptance
	complements = {'a':'t',
				'A':'T',
				't':'a',
				'T':'A',
				'g':'c',
				'G':'C',
				'c':'g',
				'C':'G'}
	#construct a new string using the dictionary to translate, then revere it with the slice
	return ''.join([complements.get(char,char) for char in pattern])[::-1]

def pattern_match(pattern, genome):
	'''
	if the pattern is found in the genome, return the indices that it is found at.
	if not, return an empty list
	'''
	indices = []
	pattern_length = len(pattern)
	for i in range((len(genome) - pattern_length) + 1):
		if genome[i:i + pattern_length] == pattern:
			indices.append(i)
	return indices

def clump_finding(genome, k, L, t):
	'''
	Searches substrings of length L in genome for all k-mers that occur at least t times
	'''
	clumps = []
	#for all substrings of length L in genome
	for i in range((len(genome) - L) + 1):
		#for all patterns in each substring
		searched_words = []
		for j in range(L - k + 1):
			pattern = genome[j:j + k]
			if pattern in searched_words or pattern in clumps:
				continue
			occurences = count(genome[i:i + L],pattern)
			if occurences >= t:
				clumps.append(pattern)
			searched_words.append(pattern)
	return clumps	




