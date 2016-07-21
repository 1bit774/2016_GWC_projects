start = '''
You have entered a adventure game. Your level is lv.1 right now. 
You see a monster that's huge and dangerous-looking coming your way. 
What should you do?
'''


print(start)

done = False
gameover= False
while done==False:
	print("Type RUN or STAND THERE")
	user_input = input()
	if user_input == "RUN":
		print("You decide to RUN and the monster sees you so it starts chasing you. What will you do now?") 
		print("Type KEEP RUNNING or FIGHT")
		user_input=input()
		if user_input== "KEEP RUNNING":
			print("You KEEP RUNNING and the monster starts speeding up, but it runs too fast that it trips on it's own feet and dies.")
			done = True
		elif user_input == "FIGHT":
			print("You choose to FIGHT. It turns out the monster was a BOSS monster whose level is 99. What were you thinking choosing to FIGHT it? You are only lv.1, so there's no way you can FIGHT. Since you chose FIGHT, you battle the monster and DIED.")
			print("GAME OVER")
			gameover = True
	elif user_input == "STAND THERE":
		print("You choose to STAND THERE and the monster gets distracted by you so it trips on its feet and dies.")
		done = True
	if done== True:
		Title_gained = '''At that exact moment, a person from the nearby town walks by. 
He thinks you defeated the monster and runs back to the town to tell the townspeople. 
They drag you back to their town and hold a party to celebrate your defeat of the monster. 
At the end of the party, they give a badge that will give you the title of the "HERO." 
If you accept this badge, you will get the responsibility of being a "HERO" and 
there will be many challenges ahead....What will you do? '''
		print(Title_gained)
 
		print("Type ACCEPT or DON'T ACCEPT")
		user_input = input()
		if user_input == "ACCEPT":
			print('You have ACCEPTED the badge. You now have the title of "HERO" and will be KNOWN as the "HERO". Leveled up to 5! The townspeople gives you a QUEST. Do you accept?') 
			done = True
		elif user_input == "DON'T ACCEPT":
			print('''You choose DON'T ACCEPT because you don't want the responsibility, but since the townspeople threw such a huge party, it attracted many people from different towns. By the end of the party, almost everybody knows that you defeated the monster(even if you didn't because it just tripped on its on feet and died). Because of the assumtion that you defeated the monster, people start calling you "HERO" Congrats! You have become the "HERO"''')
	if gameover == True:
		done= True

	



