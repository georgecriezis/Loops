sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

# 1. Function to calculate 10%
def get_commission(money):
    return money * 0.10

# 2. Create a dictionary to hold the results
commissions = {}

for name in sales:
    amount = sales[name]
    commissions[name] = get_commission(amount)

# 3. Create the Leaderboard
# This looks at our commissions and sorts them by the amount (value)
# reverse=True puts the biggest number at the top
leaderboard = sorted(commissions.items(), key=lambda item: item[1], reverse=True)

print("--- Commission Leaderboard ---")

# 4. Print the ranked list
for name, amount in leaderboard:
    print(f"{name}: ${amount}")


  