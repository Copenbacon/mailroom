"""Tests for the Main module."""
import pytest


MAIN_INPUT_TABLE = [
    [1, "Conor Clary", "Apr 2014", 200, '''Dear Conor Clary,
    Thank you for your continued generous support in Apr 2014. We hope you have a fantastic year and we look forward to your continued generous support.'''],
]

SEND_THANKS_TABLE = []
DONATION_PROMPT_TABLE = []
DONATION_DATE_TABLE = []
CREATE_REPORT_TABLE = []


@pytest.mark.parametrize("answer, result", MAIN_INPUT_TABLE)
def test_main(answer, result):
    """Test the main function."""
    from main import main
    assert main() == result


@pytest.mark.parametrize("thanking_donor, ty_answer, result", SEND_THANKS_TABLE)
def test_send_thanks(thanking_donor, ty_answer, result):
    """Test the send thanks function."""
    from main import send_thanks
    assert send_thanks(thanking_donor, ty_answer) == result


@pytest.mark.parametrize("ty_answer, result", DONATION_PROMPT_TABLE)
def test_donation_prompt(ty_answer, result):
    """Test the donation prompt function."""
    from main import donation_prompt
    assert donation_prompt(ty_answer) == result


@pytest.mark.parametrize("donation_amt, ty_answer, result", DONATION_DATE_TABLE)
def test_donation_date(donation_amt, ty_answer, result):
    """Test the donation date function."""
    from main import donation_date
    assert donation_date(donation_amt, ty_answer) == result


@pytest.mark.parametrize("donors, result", CREATE_REPORT_TABLE)
def test_create_report(donors, result):
    """Test the create report function."""
    from main import create_report
    assert create_report(donors) == result


def test_quit_script():
    """Test the quit script function."""
    from main import quit_script
    import sys
    assert quit_script() == sys.exit(0)
