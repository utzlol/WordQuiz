import random, ast, sys, time
from termcolor import colored

status_add = 0
status_del = 0
recent_add = ''

if len(sys.argv) == 2:
	
	if sys.argv[1] == "-d":
		read = open("word.txt","r")
		a_result = str(read.read())
		read.close()
		print(a_result)
		a_result_dict = ast.literal_eval(a_result)
		while True:
			del_1 = input("Which one? : ")
			if del_1 == "exit":
				sys.exit()

			if del_1 not in a_result:
				print('Not found!')
			else:
				del_2 = a_result_dict.get(del_1)
				print(f"Deleting {del_1} and {del_2}")
				del a_result_dict[del_1]
				del a_result_dict[del_2]
				print(a_result_dict)
				write = open("word.txt","w")
				write.write(str(a_result_dict))
				write.close()
	
	elif sys.argv[1] == "-a":
	
		read = open('word.txt', 'r')
		print(read.read())
		read.seek(0)
		a_result = str(read.read())
		a_result_raw_dict = ast.literal_eval(a_result)
		a_result_raw_dict = a_result_raw_dict.values()
		print("\n\n\n\n\n")
		print(a_result)
		read.close()

		if "{" not in a_result:
			a_result = "{"+a_result
		a_result = a_result.replace('}', '')
		a_result_raw = a_result
		print(a_result)
		print('Create Mode Active!')
		
		while True:
			a_recent_add_dict = ''
			same_word = 0
			fill_word = 0
			execute_same_word = 1
			same_recent_word = 0
			
			add_check = input('Sure? (Y/n) ').lower()
			if add_check == "y" or add_check == "":
				first_d = input('1 : ')
				second_d = input('2 : ')
				
				if len(first_d) != 0 and len(second_d) != 0:
					fill_word = 1
					
				if first_d in a_result_raw_dict or second_d in a_result_raw_dict:
						same_word = 1
						execute_same_word = 0

				if len(str(recent_add)) != 0:
						a_recent_add_dict = '{'+recent_add+'}' 
						a_recent_add_dict = a_recent_add_dict.replace(',,',',').replace('{,','{').replace(',}','}')
						a_recent_add_dict = ast.literal_eval(a_recent_add_dict)
						a_recent_add_dict = a_recent_add_dict.values()
						if first_d in a_recent_add_dict or second_d in a_recent_add_dict:
							same_recent_word = 1
						
				if fill_word == 1 and same_word == 0 and same_recent_word == 0:
					status_add = 1
					first_p = ",'"+first_d+"':'"+second_d+"',"
					second_p = ",'"+second_d+"':'"+first_d+"',"
					recent_add = recent_add+first_p+second_p
					print(first_p)
					print('\n')   
					a_result = a_result+first_p+second_p
				elif same_word == 1:
					print("You fill with the exist string in the dictionary")
				elif same_recent_word == 1:
					print(first_d+":"+second_d+" have been added to the recent dictionary")
					print(a_recent_add_dict)
				else:
					print('Please fill both input!')
			elif add_check == "n" or "s":
				if status_del == 1:
					if len(recent_add) != 0:
						a_result = a_result_raw+recent_add
					else:
						print("Nothing changed!")
						sys.exit()
					
				if status_add == 1:
					if "{," in a_result:
						a_result = a_result.replace("{,","{")
					a_result = a_result+"}"
					a_result = a_result.replace(',}','}').replace(',,',',')
					print(a_result)
					write_dict = open('word.txt','w')
					write_dict.write(a_result)
					sys.exit()
				else:
					print('Nothing changed')
					sys.exit()
			
			elif add_check == "d":
				recent_add = "{"+recent_add+"}"
				recent_add = recent_add.replace("{,","{").replace(",}","}").replace(',,',',')
				recent_add = ast.literal_eval(recent_add)
				print(recent_add)
				del_1 = input("Which one? : ")
				if recent_add.get(del_1) == None:
					print("Not Found!")
				else:
					del_2 = recent_add.get(del_1)
					print(f"Deleting {del_1} and {del_2}")
					time.sleep(1)
					del recent_add[del_1]
					del recent_add[del_2]
					print(recent_add)
					recent_add = str(recent_add)
					recent_add = recent_add.replace("{",",").replace("}",",")
					if recent_add == ",,":
						recent_add = ""
					status_del = 1
					print(recent_add)
				
			
			else:
				print('Please write correctly!')
	else:
		print('Argument not found!')
		sys.exit()
	
if len(sys.argv) > 2:
	print('too much argument!')

turn = 0
showed_word = ['','','','','','','','','','']

with open("word.txt","r") as wrd:
	lsf = wrd.read()
	ls = ast.literal_eval(lsf)
while True:
	same_showed_word = 0
	rc = random.choice(list(ls))
	if rc not in showed_word:
		print(colored(rc, "blue"))
		q = input("Ready?")
		if len(q) > 0:
			break
		print(colored(ls.get(rc), "yellow"))
		print('\n')
		print("--------------")
		print('\n')
	else:
		same_showed_word = 1
			
	if len(rc) != 0 and same_showed_word == 0:
		if turn == 9:
			showed_word[turn] = rc
			turn = 0
	
		elif turn == 8:
			showed_word[turn] = rc
			turn = turn + 1
		
		elif turn == 7:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 6:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 5:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 4:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 3:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 2:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 1:
			showed_word[turn] = rc
			turn = turn + 1
		elif turn == 0:
			showed_word[turn] = rc
			turn = turn + 1

