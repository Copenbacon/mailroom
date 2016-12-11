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

email_template_first_timer = '''Dear {donor},
    Thank you for your generous support in {recent_year}. We hope you have a fantastic year and we look forward to your continued generous support.'''

email_template_non_virgin = '''Dear {donor}, 
    Thank you for your continued generous support in {recent_year}. We hope you have a fantastic year and we look forward to your continued generous support.'''


def main():
    """The main function of this module."""
    question = """How can I help you today?
    [1]Send a Thank You
    [2]Create a Report
    [3]Quit Mailroom
    """
    answer = str(input(question))
    if answer == '1':
        do_this = thank_you()
    elif answer == '2':
        do_this = create_report(DONORS)
    elif answer == '3':
        do_this = quit_script()
    else:
        print('Invalid Answer')
        do_this = main()
    return do_this()


def thank_you():
    """Run this function when SEND A THANK YOU is chosen."""
    ty_answer = str(input("Please enter a name or type 'list' to receive a list of donor names. Type 'cancel' to go back to main menu "))
    ty_answer = ty_answer.title()
    if ty_answer.lower() == 'cancel':
        main()
    elif ty_answer.lower() == "list":
        donors_list = list(DONORS)
        for i in range(len(donors_list)):
            print(donors_list[i])
            thank_you()
    elif ty_answer.title() not in DONORS.keys():
        DONORS.setdefault(ty_answer, {'': ''})
        donation_prompt(ty_answer)
        DONORS[ty_answer].pop("")
        thanking_donor = DONORS[ty_answer]
    else:
        donation_prompt(ty_answer)
        thanking_donor = DONORS[ty_answer]
    return send_thanks(thanking_donor, ty_answer)


def send_thanks(thanking_donor, ty_answer):
    """Print out an email thanking donor."""
    if len(list(thanking_donor)) > 1:
        print(email_template_non_virgin.format(donor=ty_answer, recent_year=list(DONORS[ty_answer].keys())[0]))
    else:
        print(email_template_first_timer.format(donor=ty_answer, recent_year=list(DONORS[ty_answer].keys())[0]))
    main()


def donation_prompt(ty_answer):
    """Prompt for donation amount and date."""
    import math
    donation_amt = input('''How much did {donor} donate? Type "cancel" to return to main menu.
        '''.format(donor=ty_answer))
    if donation_amt.lower() == 'cancel':
        main()
        # break
    while True:
        try:
            math.isnan(float(donation_amt))
            break
        except ValueError:
            print('That is not a valid number, please enter an integer or floating decimal ')
            donation_prompt(ty_answer)
    return donation_date(donation_amt, ty_answer)


def donation_date(donation_amt, ty_answer):
    """Update Donors list with new donation date and amount for donor."""
    donation_date = input('When did they donate? (Please keep our db clean by adding in the Mon YYYY e.g "Dec 2016"). Type "cancel" to return to main menu. ')
    if donation_date.lower() == 'cancel':
        main()
    print(DONORS)
    DONORS[ty_answer].update({donation_date: int(donation_amt)})
    print(DONORS, 'DONORS Updated')
    return DONORS


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
    main()


def quit_script():
    """End the script."""
    import sys
    return sys.exit(0)


if __name__ == '__main__':
    main()
