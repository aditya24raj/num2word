#range(0,20,1) with their word form
nw019={"0":"","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen","17":"Seventeen","18":"Eighteen","19":"Nineteen"}

#range(20,100,10) with their word form 
nw2090={"2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty","7":"Seventy","8":"Eighty","9":"Ninety"}

#place values' position and place Values' word form
#to increase max supported digits, add position and name of that
#place Values 
place={"":(None,-2)," Hundred ":(-2,-3)," Thousand ":(-3,-5)," Lakh ":(-5,-7)," Crore ":(-7,-9)}


#numPart is min 1 max 2 digits number
#numPart if less than 19 is directly converted using nw019 dictionary
#if greater than 19, ex 23, 2 is converted using nw2090 and 3 is by nw019
#the word form is returned ex Nineteen, TwentyThree
def ToWord(numPart):
	if int(numPart)<=19:
		return nw019[numPart]
	else:
		return nw2090[(numPart)[0]]+nw019[(numPart)[1]]
		


#using place dictionary keys, ex(-2,None), we split num in numPart and convert
#numPart to word by ToWord() then add relative place dictionary value to it,ex lakh.
#placeCurrent value changes to last maximum place absolute(+ive) key
#when placeCurrent values exceeds length of number itself,i.e. 
#all digits are converted, loop is breaked
def WordAssembler(num):
	placeCurrent=0
	word=""
	
	if int(num)!=0:
		for placeName,placePosition in place.items():
			
			numPart=(num[placePosition[1]:placePosition[0]])
			wordPart=ToWord(numPart)
		
			if wordPart!="":
				word=wordPart+placeName+word	
		
			placeCurrent=abs(placePosition[1])
			if placeCurrent>=len(num):
				break
	else:
		word="Zero"
		
	print("Word:",word,"\n")
	

#Returns an string value with digits 
#less than maxLen
#maxLen is length digits that can be converted

def TakeInput(maxLen):
	try:
		num=int(input("Number[1-9 digits]: "))
		if len(str(num))>maxLen:
			print("Error: Sorry, Only Numbers Upto {} Digits Are Allowed".format(maxLen))
			exit()
	except ValueError:
		print("Error: Invalid Integer!\n")
		exit()
	
	return str(num)

#declare maxLen, maximum digits supported
maxLen=9

#give WordAssembler() the value returned by TakeInput() 
WordAssembler(TakeInput(maxLen))
