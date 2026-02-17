def main():
    # our data: revenue for each year (in thousands)
    revenue_data = [3, 5, 8, 10, 14]

    print(" Startup Revenue Projection ")
    print(" (Each # represents $1,000) ")

    # Loop through the data
    for i in range(len(revenue_data)):
        # Calculate the year (i + 1)
        year = i + 1

        # Get the value from the list using the index
        value = revenue_data[i]

        bar = "#" * value  # Create a bar of '#' characters based on the value

        print(f'Year {year}: {bar} (${value}k)')
main()