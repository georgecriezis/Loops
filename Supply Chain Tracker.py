# Model a list of warehouses, each with an inventory dictionary
def main():
    warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]
    # a dictionary to store grand totals
    totals = {}

    # go to each warehouse one by one
    for warehouse in warehouses:
        inventory = warehouse["inventory"]

        # look at each item in that warehouse
        for product, count in inventory.items():
            # if the product is already in our totals, add to it
            if product in totals:
                totals[product] += count
            # if it is not a new product, start the count
            else:
                totals[product] = count
    # print the grand totals
    print("Total Supply Chain Inventory:")
    for product, total_count in totals.items():
        print(f"{product.capitalize()}: {total_count}")
main()