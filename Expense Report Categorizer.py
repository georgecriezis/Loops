# simulate an employee submitting expenses across categories (travel, meals, supplies)
# store expenses in a dictionary
# loop through and compute category totals and the grand total

def main():
    expenses = {
        "Travel": [500, 200],
        "Meals": [40, 60, 30],
        "Supplies": [100]
    }

    grand_total = 0

    print("Expense Report Summary:")
    # Loop through each category
    for category in expenses:

        # get the list of numbers for this category
        receipts = expenses[category]

        # use sum() to add up all the numbers in that list at once
        category_total = sum(receipts)

        # add this to our big total
        grand_total += category_total
    
        print(f"{category} total: ${category_total}")

    print(f"Grand total: ${grand_total}")
main()
