"""The main file for our Mailroom App."""
DONORS = {
    "Regenal Grant": {
        "Jan 2016": 200,
        "May 2015": 100,
        "Jan 2014": 50,
        "Dec 2013": 25,
    },

    "Conor Clary": {
        "Feb 2016": 25,
        "Mar 2015": 114,
        "Dec 2014": 37,
        "Nov 2013": 2,
    },

    "Dave Hume": {
        "Aug 2016": 125,
        "Apr 2015": 359,
        "Jan 2014": 378,
        "Sep 2013": 2450,
        "Nov 2012": 2,
    },

    "Chris Ladoux": {
        "Nov 2002": 20000,
    },
}


def main():
    """The main function of this module."""
    question = """How can I help you today?
    [1]Send a Thank You
    [2]Create a Report
    [3]Quit Mailroom
    """
    answer = input(question)
    if answer == '1':
        thank_you()
    elif answer == '2':
        create_report(DONORS)
    elif answer == '3':
        quit_script()
    else:
        print('Invalid Answer')
        main()


def thank_you():
    """Run this function when SEND A THANK YOU is chosen."""
    ty_answer = input("Please enter a name or type 'list' to recieve a list of donor names. Type 'cancel' to go back to main menu ")
    if ty_answer.lower() == 'cancel':
        main()
    elif ty_answer.lower() == "list":
        donors_list = list(DONORS)
        for i in range(len(donors_list)):
            print(donors_list[i])
            thank_you()
    elif ty_answer not in DONORS:
        donation_amt = input("I don't see them in here. How much did they donate? ")
        donation_date = input("and when did they donate? ")
        DONORS.set_default(ty_answer, {donation_date: int(donation_amt)})
        thanking_donor = DONORS[ty_answer]
    else:
        print(DONORS[ty_answer])
        thanking_donor = DONORS[ty_answer]
    return thanking_donor


def donation_prompt(thanking_donor):
    """Prompt for donation amount and date."""
    import math
    donation_amt = input('''How much did {donor} donate? Type "cancel" to return to main menu.
        '''.format(donor=thanking_donor))
    if donation_amt.lower() == 'cancel':
        main()
        # break
    while True:
        try:
            math.isnan(float(donation_amt))
            break
        except ValueError:
            print('That is not a valid number, please enter an integer or floating decimal ')
            donation_prompt(thanking_donor)
    return donation_date(donation_amt, thanking_donor)


def donation_date(donation_amt, thanking_donor):
    """Update Donors list with new donation date and amount for donor."""
    donation_date = input('When did they donate? (Please keep our db clean by adding in the Mon YYYY e.g "Dec 2016"). Type "cancel" to return to main menu. ')
    return DONORS[thanking_donor].update({donation_date: donation_amt})


def create_report(donors):
    """Print out a report of Donor performance."""
    donors_list = []
    # Iterate over Donor keys, sum total money, append Donor and sum to list.
    for key in DONORS.keys():
        money = 0
        for value in DONORS[key]:
            money += (DONORS[key][value])
        donors_list.append((key, money,))
    # Sort donors list by money in tuple (tup[1]) descending.
    donors_list2 = sorted(donors_list, key=lambda tup: tup[1], reverse=True)
    print("\033c")
    print(("{:^20} | {:^20} | {:^20} | {:^20}").format('Donor Name', 'Total Money Donated', 'Times Donated', 'Avg Donation Amount'))
    # Print it all out + total donations and avg donation amount.
    for tup_of_name_and_money in donors_list2:
        for idx in range(0, len(tup_of_name_and_money), 2):
            print_name = tup_of_name_and_money[idx]
            total_money_donated = tup_of_name_and_money[idx + 1]
            total_times_donated = len(DONORS[tup_of_name_and_money[idx]])
            avg_donation_amt = total_money_donated / total_times_donated
            print_total_money = str(total_money_donated)
            print_total_times = str(total_times_donated)
            print_avg = str(avg_donation_amt)
            print(("{:<20} | {:^20} | {:^20} | {:^20}").format(print_name, print_total_money, print_total_times, print_avg))
    # for key in DONORS.keys():
    #     for value in DONORS[key]:
    #         # donors_list3.append((key, DONORS[key][value],))
    #         print(key + ' ' + str(DONORS[key][value]))


def quit_script():
    """End the script."""
    import sys
    return sys.exit(0)

# def list_of_donors(donors):
#     """Create a list of Donors."""
#     donors_list = list(DONORS)
#     donors_list.sort()
#     return donors_list

if __name__ == '__main__':
    main()
