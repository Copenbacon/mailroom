"""The main file for our Mailroom App."""
DONORS = {
    "Regenal Grant": [{
        "Jan 2016": 200,
        "May 2015": 100,
        "Jan 2014": 50,
        "Dec 2013": 25,
    }],

    "Conor Clary": [{
        "Feb 2016": 25,
        "Mar 2015": 114,
        "Dec 2014": 37,
        "Nov 2013": 2,
    }],

    "Dave Hume": [{
        "Aug 2016": 125,
        "Apr 2015": 359,
        "Jan 2014": 378,
        "Sep 2013": 2450,
        "Nov 2012": 2,
    }],

    "Chris Ladoux": [{
        "Nov 2002": 20000,
    }]
}


def main():
    """The main function of this module."""
    import inquirer
    question = [
        inquirer.List('Prompt', message="How can I help you today?", choices=["Send a Thank You", "Create a Report"]),
    ]
    answer = inquirer.prompt(question)
    answer = answer['Prompt']
    return answer
    quit_script(answer)
    if answer == 'Send a Thank You':
        thank_you()
    elif answer == 'Create a Report':
        create_report()
    else:
        main()
