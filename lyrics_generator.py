

def generate_lyrics (file,lines,print_or_not):
	
	#importing markovify 
	import markovify 
	
	#seting dataset 
	dataset = file
	
	#setting text model 
	text_model = markovify.Text(dataset)
	
	#creating new lyrics 
	lyrics = []
	
	
	for i in range(lines):
		x= text_model.make_sentence()
		if x :
						lyrics.append(x)
	
	#printing 
	if print_or_not == 1 :
		#printing new lyrics 
		for i in lyrics:
			print(i)
			
	#returning 
	return lyrics



		
		
		