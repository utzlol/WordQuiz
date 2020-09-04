import random, ast
from termcolor import colored
with open("word.txt","r")
        lsf = wrd.read()
        lsl = lsf
        ls = ast.literal_eval(lsl)
while True:
	rc = random.choice(list(ls))
	print(colored(rc, "blue"))
	q = input("Ready?")
	if len(q) > 0:
		break
	print(colored(ls.get(rc), "yellow"))
	print("--------------")
