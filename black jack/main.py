import random
user_cards=[]
computer_cards=[]
should_continue=True
def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card=random.choice(cards)
	return card
for i in range(2):
	user_cards.append(deal_card())
	computer_cards.append(deal_card())
def calculate_score(cards):
	if len(cards)==2 and sum(cards)==21:
		return 0
	if 11 in cards and sum(cards) > 21 :
		cards.remove(11)
		cards.append(1)
	return sum(cards)
def compare(user_score,computer_score):
	if user_score==computer_score:
		return("Its a tie")
	elif computer_score==0 :
		return("You lose, opponent has black jack!")
	elif user_score>21:
		return"You went over 21\nBUSTED!!!!!"
	elif user_score ==0 :
		return"Win with a black jack!"
	elif computer_score>21:
		return"Opponent went over 21, You win"
	else:
		if user_score>computer_score:
			return("You won")
		else:
			return("You lose")
while should_continue== True:
	user_sum=calculate_score(user_cards)
	computer_sum=calculate_score(computer_cards)
	print(f"   Your Cards: {user_cards}, current score: {user_sum}\n   Computer's first cards: {computer_cards[0]}")
	if user_sum==0 and computer_sum==0 or user_sum>21:
		should_continue = False
	else:
		draw=input("Do you want to draw another card? \n'y'or'n': ")
		if draw == "y":
			user_cards.append(deal_card())
		elif draw == "n":
			should_continue=False
while computer_sum!=0 and computer_sum<17:
	computer_cards.append(deal_card())
	computer_sum=calculate_score(computer_cards)
print(f"   Your final hand: {user_cards}, final score: {user_sum}\n   Computer'final hand: {computer_cards}, computer's score: {computer_sum}")
print(compare(user_sum, computer_sum))
