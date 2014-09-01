# 1. generate word
import random
from urllib.request import urlopen
LIMIT = 10
#words = open('/usr/share/dict/words').read().split()
words = urlopen("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt").read().split()
words = [word.decode('utf-8') for word in words if len(word) > 4]

thisword = (random.choice(words)) 

slots = ["_"] * len(thisword)
wrong_guess = []
guesses = []

def find_all_indices(word, letter):
	"""
	Finds the indices of all occurrences of letter in word.
	>>> find_all_indices("viola", "a")
	[4]
	>>> find_all_indices("apple", "p")
	[1, 2]
	>>> find_all_indices("hippopotamus", "p")
	[2, 3, 5]
	"""
	list_indices = []
	current_index = 0
	while word.find(letter) > -1:
		index = word.find(letter)
		list_indices.append(current_index + index)
		word = word[index+1:]
		current_index = current_index + index + 1
	return list_indices


while len(wrong_guess) < LIMIT and "_" in slots:
	print(" ".join(slots))
	letter = input('Next guess> ')
	if letter in guesses:
		print("Don't guess something you already guessed")
		continue
	guesses.append(letter)
	if letter in thisword:
		indices = find_all_indices(thisword, letter)
		for index in indices:
			slots[index] = letter
	else:
		wrong_guess.append(letter)
	print(wrong_guess)
if "_" in slots:
	print("You lose sucker.")
else:
	print("Congrats, you won!")
print(thisword + " was the word.")


# 2. write number of slots

# 3. person guesses a letter.
# if right, letter is displayed in slots
# if wrong, show wrong guess. keep track 
# of the # of guesses b/c you only can get __ wrong.
# display slots always

#person guesses until he gets the word or dies 