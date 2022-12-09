# Challenge 1

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter you DOB in the format DD Mmm YYYY: \n")
date_object = datetime.strptime(date_input, '%d %b %Y')
print ("The year entered is ", date_object.year, "\n")
print("125 days ago my age was ", datetime.today() - timedelta(days=125), ".\n")


# Challenge 2 

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter your booking date in format DD Mmm YYY: \n")
date_object = datetime.strptime(date_input, '%d %b %Y')
print ("The year entered is ", date_object.year, "\n")
print("In two weeks it will be ", datetime.today() + timedelta(weeks=2), ".\n")

