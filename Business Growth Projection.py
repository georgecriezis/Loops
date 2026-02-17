def main():
    # 1. Get input from the user
    # We use float() so they can type decimals
    revenue = float(input("Enter initial revenue (e.g., 10000): "))
    growth_rate = float(input("Enter growth rate as a decimal (e.g., 0.05 for 5%): "))

    print("\n--- 10-Year Business Growth Projection ---")
    print(f"{'Year':<10} | {'Revenue':<15}")
    

    # 2. Loop 10 times (Year 1 through Year 10)
    for year in range(1, 11):
        
        # Calculate growth for this year
        # New Revenue = Old Revenue + (Old Revenue * Growth Rate)
        revenue = revenue * (1 + growth_rate)
        
        # 3. Print the result in a neat table format
        # :<10 makes the column 10 spaces wide
        # :.2f makes it show 2 decimal places like money
        print(f"Year {year:<5} | ${revenue:,.2f}")

main()