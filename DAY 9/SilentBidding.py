dict = {}
# from replit import cleared
# from art import logo
# print(logo)
while True:
    name = input("Enter the bidder name : ")
    bid = int(input("Enter your bid in : $"))
    dict[name] = bid
    choice = input("Any other person left Y or N :")
    if choice=='N':
        break
max_bid = 0
winner = ""
for bidder in dict:
    if dict[bidder] > max_bid:
        max_bid = dict[bidder]
        winner = bidder

print(f"winner of the bidding {winner} with highest bid of ${max_bid}")
