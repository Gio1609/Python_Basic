#Function frequency characters
def char_frequency(str1):
	dict = {}
	for c in str1:
		if(c in dict.keys()):
			dict[c]+=1
		else:
			dict[c]=1
	return dict

print(char_frequency("google.com"))