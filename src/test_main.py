"""Tests for the Main module."""
import pytest


def test_main():
    """Test the main function."""
    from main import main
    assert main() == "Send a Thank You" or "Create a Report"