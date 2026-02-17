def main():
    # 1. Customer data: Name and how much they spent
    customers = {
        "Alice": 1200,
        "Bob": 450,
        "Charlie": 6000,
        "David": 2500,
        "Eve": 800
    }

    # 2. Tally sheet to count how many people are in each tier
    tier_counts = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }

    # 3. Loop through customers to check their spending
    for name in customers:
        spending = customers[name]

        # 4. Use conditionals (if/elif/else) to assign a tier
        if spending >= 5000:
            tier_counts["Gold"] += 1
        elif spending >= 1000:
            tier_counts["Silver"] += 1
        else:
            tier_counts["Bronze"] += 1

    # 5. Print the summary
    print("Loyalty Tier Summary ")
    for tier, count in tier_counts.items():
        print(f"{tier}: {count} customers")

main()