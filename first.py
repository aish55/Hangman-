import random
possible= ["AISWARYA","IYYAPPAN","BLUE","RED","YELLOW"]
random.shuffle(possible)
answer=list(possible[1])
#print(answer)
display=[]
display.extend(answer)
for i in range (len(display)):
	display[i] = "_"
print("welcome to hangman\n")
print (' '.join(display))
print("\n\n\n\n")
count = 0
while count < len(answer):
	guess= input("please guess a letter")
	guess= guess.upper()
	for i in range (len(answer)):
	  if answer[i] == guess:
	    display[i] =guess
	    count += 1
	    print(' '.join (display))
	    print("\n\n\n")
print ("you guessed it !!!")
print(' '.join (display))