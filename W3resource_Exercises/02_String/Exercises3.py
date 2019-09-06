#Function reverse full name
def reverse_name(name):
	for word in name.split('\n'):
		return (' '.join(word.split()[::-1]))

print(reverse_name("Le Hong Phong"))