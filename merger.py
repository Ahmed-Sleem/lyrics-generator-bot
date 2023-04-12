#to get lyrics 
import lyrics_generator as lg
#to rhyme 
import get_rhymes as rh


def generate_rhymed_lyrics(file,amount):
		
	#generate some lyrics 
	lyrics = lg.generate_lyrics(file, amount, 0)
	
	#list to store the rhymed lyrics
	lyrics_rhymed = []
	
	#for every line in generated lyrics 
	for i in lyrics:
		
		#remove i from list 
		lyrics.remove(i)
		#split 
		i = i.split(" ")
		#get length 
		length = len(i) -1
		#get the last word 
		last = i[length]
		#get words that rhymes with last word 
		rh_list = rh.get_rhymes(last)
		
		#for every line in lyrics 
		for x in lyrics:
			
			#split 
			x = x.split(" ")
			#get length 
			length = len(x) -1
			#get last word 
			last2 = x[length]
			
			#for every rhymed word 
			for y in rh_list:
				#if the rhymed word = the last word in lyrical line 
				if last2 == y:
					
					#save the fist line after check for dublicants 
					if i not in lyrics_rhymed:
						lyrics_rhymed.append(i)
					
					
						#save the line that rhymed with it after check for dublicants 
						if x not in lyrics_rhymed:
							lyrics_rhymed.append(x)
				
			
		return lyrics_rhymed


def lyrics(file,amount):
	
	#get lyrics 
	ly = generate_rhymed_lyrics(file, amount)
	
	#clean lyrics 
	for i in ly :
		i = str(i)
		i = i.replace("[", "")
		i = i.replace("]", "")
		i = i.replace(",", "")
		i = i.replace("'", "")
		i = i.replace('"', "")
		print(i)
		
		return ly 
	
	