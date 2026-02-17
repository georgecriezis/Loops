def main():
    loan_amount = float(input("How much is the loan (e.g., 10000)? "))
    interest_rate = float(input("What is the interest rate (e.g., 0.05 for 5%)? "))
    monthly_payment = float(input("What is the monthly payment (e.g., 200)? "))

    monthly_rate = interest_rate / 12
    months = 0 # This starts at 0

    print("\nREPAYMENT SCHEDULE")

    while loan_amount > 0:
        # 1. Update the counter here!
        months += 1
        
        interest = loan_amount * monthly_rate
        loan_amount += interest
        loan_amount -= monthly_payment

        # 2. Use the 'months' variable to show the current month
        if loan_amount > 0:
            print(f"Month {months}: Remaining balance: ${loan_amount:.2f}")
        else:
            print(f"Month {months}: Loan paid off!")
        
        # 3. Move the summary print statement OUTSIDE the while loop
        # so it only prints once at the end.

    # 4. Final Summary (outside the loop)
    print("-" * 25)
    print(f"It took {months} months to pay off the loan.")

main()