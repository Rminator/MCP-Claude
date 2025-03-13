#!/usr/bin/env python3
"""
Test script for the leap_year module.

This script demonstrates how to use the leap_year module to check for leap years
and find leap years within a range.
"""

import leap_year

def main():
    # Test individual years
    test_years = [1900, 2000, 2020, 2023, 2024, 2025, 2028, 2100]
    
    print("Testing individual years:")
    for year in test_years:
        if leap_year.is_leap_year(year):
            print(f"  ✓ {year} is a leap year")
        else:
            print(f"  ✗ {year} is not a leap year")
    
    print("\nFinding leap years in a range:")
    # Find leap years in the first quarter of the 21st century
    century_leap_years = leap_year.find_leap_years(2000, 2025)
    print(f"  Leap years from 2000 to 2025: {century_leap_years}")
    
    print("\nFinding next leap year:")
    current_year = 2025
    next_leap = leap_year.get_next_leap_year(current_year)
    print(f"  Next leap year after {current_year}: {next_leap}")
    
    print("\nFinding previous leap year:")
    prev_leap = leap_year.get_previous_leap_year(current_year)
    print(f"  Previous leap year before or including {current_year}: {prev_leap}")

if __name__ == "__main__":
    main()
