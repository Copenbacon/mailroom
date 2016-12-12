"""Tests for the Main module."""
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


def test_send_thanks():
    """Test the send_thanks func."""
    from main import send_thanks
    assert send_thanks('"Chris Ladoux": {"Nov 2002": 20000, }', 'Chris Ladoux') == """Dear Chris Ladoux,
    Thank you for your continued generous support in Nov 2002. We hope you have a fantastic year and we look forward to your continued generous support."""


def test_create_report():
    """Test the Create Report Function."""
    from main import create_report
    assert create_report(DONORS) == [('Chris Ladoux', 20000), ('Dave Hume', 3314), ('Regenal Grant', 375), ('Conor Clary', 178)]
