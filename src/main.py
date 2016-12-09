"""The main file for our Mailroom App."""
import inquirer
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


def main(answer):
    if answer == '1':
        thank_you()
    elif answer == '2':
        create_report(DONORS)
    elif answer == '3':
        quit_script()    
    else:
        print('Invalid Answer')


def thank_you():
    ty_answer = input("Please enter a name or type 'list' to recieve a list of donor names.")
    if ty_answer.lower() == "list":
        donors_list=list(DONORS)
        for i in range(len(donors_list)):
            print(donors_list[i])
    elif ty_answer not in DONORS:
        DONORS.set_default(answer, 0)
        thanking_donor = DONORS[answer]
    else:
        print(DONORS[ty_answer])
        thanking_donor = DONORS[ty_answer]


def create_report(DONORS):
    import pdb
    donors_list = []
    for key in DONORS.keys():
        money = 0
        for value in DONORS[key]:
            money += (DONORS[key][value])
        donors_list.append((key, money,))
    donors_list2 = sorted(donors_list, key=lambda tup: tup[1], reverse=True)
    pdb.set_trace()
    for x in donors_list2:
        for j in range(0, len(x), 2):
            print(x[j] + ' ' + str(x[j+1]) + ' ' + str(len(DONORS[key])))
    donors_list3 = []
    for key in DONORS.keys():
        for value in DONORS[key]:
            # donors_list3.append((key, DONORS[key][value],))
            print(key + ' ' + str(DONORS[key][value]))


def list_of_donors(DONORS):
    donors_list=list(DONORS)
    donors_list.sort()
    return donors_list

if __name__ == '__main__':
    """The main function of this module."""
    question = [
        inquirer.List('Prompt', message="How can I help you today?", choices=["Send a Thank You", "Create a Report"]),
    ]
    question = """How can I help you today?
    [1]Send a Thank You
    [2]Create a Report
    [3]Quit Mailroom
    """
    answer = input(question)
    main(answer)
   