#the function that take a word and return list of rhyming words 
def get_rhymes(rhyme_word):
	
	#importing request to request rhymes from the site 
	import requests
	
	#the word parameter 
	parameter = {}
	parameter['rel_rhy'] = rhyme_word
	
	#the request to get rhymes 
	req = requests.get('https://api.datamuse.com/words',parameter )
	#the json with all the rhyming words 
	rhyme = req.json()
	
	#list of rhyming words 
	words = []
	
	#insert the rhyming words in the list 
	for i in rhyme:
		words.append(i['word']) 
		
	return words




