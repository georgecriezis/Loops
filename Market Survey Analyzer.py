# students collect fake survey data: a list of customer preferences for a product (e.g., "coffee", "tea", "soda")
# use a dictionary to count how many people chose each product
# print a market-share style summary

def main():
    # survey data
    responses = ["coffee", "tea", "coffee", "soda", "coffee", "tea"]

    # create a dictionary to count votes
    tally = {}

    #count votes and convert to a percentage style summary
    for item in responses:
        if item in tally:
            tally[item] += 1 # add 1 to existing count
        else:
            tally[item] = 1 # start count at 1
    # calculate total for math
    total_votes = len(responses)
    # print summary
    print("Results ")
    for item, count in tally.items():
        percentage = (count / total_votes) * 100
        print(f"{item}: {percentage:.0f}%")
main() # call the main function to start the program