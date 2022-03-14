import re
pattern = re.compile("[a-z]+")

all_words = ['tacos', 'chili', 'beans', 'sauce', 'salsa', 'gallo', 'flour', 'maize', 'queso', 'chips', 'pinto', 'nacho', 'spicy', 'vegan', 'salad', 'sides', 'drink', 'order', 'pollo', 'asado', 'steak', 'fresh', 'juice', 'bowls', 'sodas', 'carne']

with open('words.txt','r',encoding='utf-8') as file:
	for line in file:
		line = line.lower().strip()
		if len(line)==5 and pattern.fullmatch(line) is not None:
			all_words.append(line)

with open('validGuesses.ts','w',encoding='utf-8') as file:
	file.write("export const VALID_GUESSES = [")
	for word in all_words:
		if word!='zwick':
			file.write("'"+word+"',")
		else:
			file.write("'"+word+"']")