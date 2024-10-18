print("Auction Program")
# Function to find the highest bid
def find_highest_bidder(bid_list):
    highest_bidder = bid_list[0]
    for user in bid_list:
        if highest_bidder['bid'] < user['bid']:
            highest_bidder = user
    print(f"The winner is {highest_bidder["name"]} with a bid of {highest_bidder["bid"]}")

# Program start here
continue_bidding = True
bidders = []

while continue_bidding:
    name = input("What is your name?\n")
    bid = int(input("What's you bid?\n"))
    bidders.append({"name": name, "bid": bid})

    ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ans == 'no':
        continue_bidding = False
        find_highest_bidder(bidders)