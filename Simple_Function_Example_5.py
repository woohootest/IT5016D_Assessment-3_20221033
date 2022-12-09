# Simple Function Example 5
#
# @ author: Kat
# date: 10/11/2022

def cm(feet = 0, inches = 0):
    """Convert a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 *2.54
    return inches_to_cm + feet_to_cm
cm(feet = 5)

cm(inches = 70)

cm(feet = 5, inches = 8)
