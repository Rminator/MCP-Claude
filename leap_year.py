#!/usr/bin/env python3
"""
Leap Year Calculator

This module provides functions to check if a given year is a leap year
and to find all leap years within a specified range.
"""


def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is divisible by 4, but not by 100 unless it's also divisible by 400.
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def find_leap_years(start_year, end_year):
    """
    Find all leap years within a specified range of years.
    
    Args:
        start_year (int): The starting year of the range (inclusive)
        end_year (int): The ending year of the range (inclusive)
        
    Returns:
        list: A list of all leap years in the specified range
    """
    return [year for year in range(start_year, end_year + 1) if is_leap_year(year)]


def get_next_leap_year(year):
    """
    Find the next leap year after or including the given year.
    
    Args:
        year (int): The year from which to start searching
        
    Returns:
        int: The next leap year
    """
    while not is_leap_year(year):
        year += 1
    return year


def get_previous_leap_year(year):
    """
    Find the previous leap year before or including the given year.
    
    Args:
        year (int): The year from which to start searching
        
    Returns:
        int: The previous leap year
    """
    while not is_leap_year(year):
        year -= 1
    return year


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
                next_leap = get_next_leap_year(year + 1)
                print(f"The next leap year after {year} is {next_leap}.")
        except ValueError:
            print("Please provide a valid year as an integer.")
    else:
        current_year = 2025
        print(f"Current year: {current_year}")
        if is_leap_year(current_year):
            print(f"{current_year} is a leap year.")
        else:
            print(f"{current_year} is not a leap year.")
            next_leap = get_next_leap_year(current_year + 1)
            print(f"The next leap year after {current_year} is {next_leap}.")
            
        print("\nSome recent and upcoming leap years:")
        recent_leap_years = find_leap_years(current_year - 20, current_year + 20)
        for year in recent_leap_years:
            print(f"- {year}")
