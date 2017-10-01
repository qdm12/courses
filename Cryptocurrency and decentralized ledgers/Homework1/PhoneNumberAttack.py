# Answers the question 3.a

from hashlib import sha256

stored_digests = set(['f338e1ff264d8c6d745caf27dd30a2f4eab4a138de \
                      1c32e9162a340ac8880fb9']) # sha256 of 0000500000

for i in range(pow(10,10)):
    number = str(i)
    if len(number) < 10:
        number = (10 - len(number)) * '0' + number
    print(number)
    digest = sha256(number.encode('utf-8')).hexdigest()
    if digest in stored_digests:
        print("Found number "+number+" matching digest "+digest)
        stored_digests.remove(digest)
        if len(stored_digests) == 0:
            print("All found.")
            exit(0)