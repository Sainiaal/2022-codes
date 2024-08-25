from art import logo
print(logo)
is_true=True
auction={}
def secret(n, b):
	auction[n]=(b)

input("PRESS ENTER TO START THE AUCTION")
print("\n"*50)
while is_true==True:
	name=input("what is your name\n")
	bid=int(input("how much do you wanna bid\n$"))
	secret(name, bid)
	repeat=input("are there any more bidders?\nYES or NO\n")
	if repeat=="yes" or repeat =="YES":
		print("\n"*50)
	else:
		break
highest=0

for people in auction:
	bidding=auction[people]
	if bidding > highest:
		highest=bidding
		winner=people
amount =auction[winner]
print("\n"*50)
print(f"The winner of this auction is {winner} \nThey bid {amount}")

