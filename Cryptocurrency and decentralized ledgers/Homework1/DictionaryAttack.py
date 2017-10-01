# Answers the question 4.b

from hashlib import sha1

target_digest = '13818a5684a7ed4dce8433c3f57e13b589b88852'

with open('words.txt', 'rb') as f:
	words = f.readlines()

for word in words:
	print(word)
	if sha1(word).hexdigest() == target_digest:
		print('Found password: ' + str(word))
		input('Press Enter to quit')
		exit(0)
print('Password not found in dictionary')