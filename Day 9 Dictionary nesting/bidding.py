logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid = True
dic = {}
while bid:
    name = input("What is your name: ")
    price = int(input("What's your bid($): "))
    ask = input("Are there any other bidders? Type 'y' for yes and 'n' for no:")
    dic[name]=price
    if ask=='n':
        bid=False
max_bid = max(dic.values())
print(f"The Highest bid is {max_bid} of { [key for key in dic if dic[key]==max_bid ][0]} ")
    