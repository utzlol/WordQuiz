import random
from termcolor import colored
ls = {'turmeric':'kunyit','tamarind':'asam jawa','nutmeg':'pala','oyster sauce':'saus tiram','salty soy sauce':'kecap asin','sweet soy sauce':'kecap manis','garlic':'bawang putih','ginger':'jahe','shallot':'bawang merah','cumin':'jinten','soybean':'kedelai','cassava':'singkong','taro':'talas','daun salam':'bay leaves','coriander':'ketumbar','lemongrass':'serai','galangal':'lengkuas','candlenut':'kemiri','hazelnut':'kemiri','terasi':'shrim paste','cuka':'vinegar','kacang tanah':'peanut','bayam':'spinach','terong':'eggplant','timun':'cucumber','jamur':'mushroom','labu':'pumpkin','kubis':'cabbage','rumput laut':'seaweed','lobak':'raddish','brokoli':'broccoli','kangkung':'kale','jagung':'corn','acar':'pickle','keju':'cheese','kuning telur':'yolk'}
while True:
	rc = random.choice(list(ls))
	print(colored(rc, "blue"))
	q = input("Ready?")
	if len(q) > 0:
		break
	print(colored(ls.get(rc), "yellow"))
	print("--------------")
