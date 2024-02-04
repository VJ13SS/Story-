'''This is a simple program designed to make demonstrate the flow of a basic program.The major aim of this project is to make beginners understand the working of if,if-else statements,print,input function...!
To make it interactive i had tried to tell a simple story here....Hope you enjoys it....!'''
name=input('Enter your name: ')
print('Hey welcome  ',name,'.This is an adventure game...You will be provided with certain choices which can be cumulated to make an adventureous story....')
answer=input('You are walking through your street suddenly you landed up in a maze...You want to get out. ut dont know the path..Here you can go either left or right....!which way do you choose...left or right? ').lower()
if(answer=='right'):
	answer=input('You began to move towards the right...in the way you found a medkit,food...Do you wish to take it...!(Type yes or no) ').lower()
	if(answer=='yes'):
		print('You got a bagpack with a meditkit and some food in it.....')
	answer=input('In the way on moving further you sees some  foot prints of a big unknown creature...You also sees a sword and a gun near to it...which one do you choose(gun or sword)...? ').lower()
	weapon=answer
	if(answer=='sword'):
		print('You got an armour kit including a sword...You got sone powerups like speed,strength,eagle eyes...')
	else:
		print('You got a soldier bundle with a gun in hand along with the accessories..Powerups like wit,strength,aim....')
	answer=input('You moved forward....Suddenly you noticed that the ground is shaking ...Ypu suddenly noticed that a monster is heading towards you ...It is heading to attack you.....what will you do run away or jump and attack.....').lower()
	if(answer=='run away'):
		print('You noticed that you had reached a wall and had realised that there is no way to escape....rather than to fight....So you decided to fight that demon.....')
	print(f'You jumped and is attacking the demon with your {weapon} and by utilising all your powerups.....You had finally defeated the demon....andgthen you find something shining near to the demons body....when you touched it you reached....suddenly you are in your street with the same kind of people around..,.You were back to your land..,After realising everything...you just smiled and walked away....!')
else:
	answer=input('You began to move towards left....you found a pond full of crocodiles....suddenly a rope from the sky came near to you....you can take it to reach the other end or can choose the boat lying on the pond....what will you choose...the hanging rope or the boat(Type roap or boat)? ').lower()
	if(answer=='boat'):
		print('You chose the boat to cross the sea..The crocodiles attacked you..you were cauht by them...and you passed away....')
	else:
		print('You chose the hanging rope to reach the other end....You moved further....')
		answer=input('In the way you found an armour kit which has a medkit,a sword and the armour vest in ti...Do you wish to yake it...?(Type yes or no).....').lower()
		if(answer=='yes'):
			answer=input('You moved by taking it .....')
		else:
			print('You moved further...')
		answer=input('then suddenly you found that the ground is shaking...Suddenly you found a monster in front of you.....what will you do(Type....Fight or run away)?.....').lower()
		if(answer=='fight'):
			print('You jumped to fight the monster...')
		else:
			print('You ran away from the monster...and suddenly you reached the dead end...You have no chance other than to fight the monster....')
		print('You fought the monster...and killed it..suddenly you found a white light around you and then you were suddenly in your street just like the way how it was...you just smiled and walked away')
			