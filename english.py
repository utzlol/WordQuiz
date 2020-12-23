import random, ast, sys
from termcolor import colored

status_add = 0

if len(sys.argv) == 2:
	if sys.argv[1] == "-c":
		read = open('word.txt', 'r')
		print(read.read())
		read.seek(0)
		a_result = str(read.read())
		read.close()
		a_result = a_result.replace('}', '')
		print(a_result)
		print('Create Mode Active!')
		
		while True:
			add_check = input('Sure? (Y/n) ').lower()
			if add_check == "y" or add_check == "":
				pass
			elif add_check == "n":
				print('mulai')
				if status_add == 1:
					a_result = a_result+"}"
					a_result_final = a_result.replace(',}','}').replace(',,',',')
					print(a_result_final)
					write_dict = open('word1.txt','w')
					write_dict.write(a_result_final)
					sys.exit()
				else:
					sys.exit()
			else:
				print('Please write correctly!')
				sys.exit()
			first_d = input('1 : ')
			second_d = input('2 : ')
			if len(first_d) != 0 and len(second_d) != 0:
				status_add = 1
				first_p = ",'"+first_d+"':'"+second_d+"',"
				second_p = ",'"+second_d+"':'"+first_d+"',"
				print(first_p)
				print('\n')
				a_result = a_result+first_p+second_p
			

		
		
		sys.exit()
	if sys.argv[1] == "t" :
		sys.exit()

if len(sys.argv) > 2:
	print('too much argument!')

with open("word.txt","r") as wrd:
	lsf = wrd.read()
	ls = ast.literal_eval(lsf)
while True:
	rc = random.choice(list(ls))
	print(colored(rc, "blue"))
	q = input("Ready?")
	if len(q) > 0:
		break
	print(colored(ls.get(rc), "yellow"))
	print('\n')
	print("--------------")
	print('\n')
