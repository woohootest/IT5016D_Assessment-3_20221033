# Function Example 3
#
# @ author: Kat
# date: 10/11/2022

import math
dir(math)
math.pi = 3.141592653589793
def volume(r):
    """Returns the volume of a sphee with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v
