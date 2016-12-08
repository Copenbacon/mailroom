# The script should have a data structure that holds a list of your donors and a history of the amounts they have donated.
donors = {
    "moneybags1": [{
        "june2016": "$XXXX"
        "may2016": "$XXXX"
        "jan2016": "$XXXX"
    }],

    "moneybags2": [{
        "june2016": "$XXXX"
        "may2016": "$XXXX"
        "jan2016": "$XXXX"
    }],

    "moneybags3": [{
        "june2016": "$XXXX"
        "may2016": "$XXXX"
        "jan2016": "$XXXX"
    }],
}

# When run, the script should prompt the user to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
def original_prompt():
    import inquirer
        questions = [
            inquirer.List('first run',
                message="whaddya want?"
                choices=["Send a Thank You", "Create a Report"],
            ),
        ]
        answer = inquirer.prompt(questions)
        quit_script(answer)
        if anwser == 'ty':
            run thank_you()
        elif user_prompt == 'create':
            run create_report()
        else:
            original_prompt()


# If the user selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
def thank_you():
    answer = name_prompt()
    quit_prompt(answer)
    if answer == 'list':
        run list(donors)
        thank_you()
    elif answer is not in donors:
        donors.setdefault(answer, 0)
        thanking_donor = donors[answer]
    else:
        print donors[answer]
        thanking_donor = donors[answer]
    return thanking_donor


# Once a name has been selected, prompt for a donation amount.
# Verify that the amount is in fact a number, and re-prompt if it isn’t.
# Once an amount has been given, add that amount to the donation history of the selected user.
def make_that_money(thanking_donor):
    I_want_that_money = user_prompt('how much did this idiot contribute?')
    quit_prompt(user_prompt)
    if type(I_want_that_money) is not int:
        make_that_money(thanking_donor)
    thanking_donor.update(todays_date, $$$$)
    return thanking_donor



# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
def write_email(thanking_donor):
    emailtemp = "Dear {loser}, thank you for the recent donation".format(loser=thanking_donor)
    print(emailtemp)
    original_prompt()


# You need not persist the new donors when the script quits running.
# If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly.

def create_report():
    donorslistsorted = list_of_donors()
    printout = '{name} | {total_donated} | {num_donations} | {avg_donation} /n'
    for x in donorslistsorted:
        get_donor_attributes[donors[x]]
        print(printout.format(name, total_donated, num_donations, avg_donation))

def list_of_donors()
    donorslist = []
    for i in range(donors):
        donorslist.append(donors[i])
    donorslistsorted = sorted(donorslist, historicalDonationAmt)
    return donorslistsorted

def get_donor_attributes(donors):
    donors.name = donors[name]
    donors.total_donated = sum(donors.donations)
    donors.num_donations = len(donors[name][0])
    donors.avg_donations = donors.total_donated/donors.num_donations


def quit_script(user_prompt):
    if user_prompt == "q" or "quit" or "exit":        
        return sys.exit(0)

def quit_prompt(user_prompt):
    if user_prompt == "q" or "quit" or "exit":        
        return original_prompt()
    
if __name__ == "__main__":
    original_prompt()