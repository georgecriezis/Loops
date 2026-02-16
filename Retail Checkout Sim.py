# Retail Checkout Simulation
# Asks customers to enter the price of items they're buying (look until they enter 0)
# store prices in a list, then calculate the total purchase amount, average item cost, number of items bought, and print it out

def main():
    prices = []

    while True:
        price = float(input("What is the price of the item? " ))
        if price == 0:
            break

        # if price is negative then ask again
        if price < 0:
            print("Price cannot be negative. Please enter a valid price. ")
            continue
        # Takes the number and adds it to the list of prices
        prices.append(price)

        # Check is bag is still empty
        if not prices:
            print("Your bag is empty. ")
        
        # Calculate purchase total, average item cost, and number of items bought
        total = sum(prices)
        average = total / len(prices)
        num_items = len(prices)

        print(" Check out summary: ")
        # find total purchase amount and round to 2 decimal places
        print(f"Total purchase amount: ${total:.2f}")
        print(f"Average item cost: ${average:.2f}")
        print(f"Number of items bought: {num_items}")

main()  # Call the main function to start the program
