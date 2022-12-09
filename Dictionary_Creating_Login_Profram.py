# Dictionary Creating a login program
#
# @ author: Kat
# date: 08/11/2022

print('\nThe Login Example')
#stored login credentials
loginDetails = {'user1':'apple123', 'user2':'ball456', 'user3':'coin789'}
print('\nWelcome! You have three attempts to enter your login details.')
attempt = 0
while attempt < 3:
  print('\nPlease enter your Username and Password:')
  user_name = input('\nUsername: ')
  password = input('Password: ')
  success = False
  for key,value in loginDetails.items():
    if (key == user_name 
       and value == password):
         success = True
         break
  attempt += 1
  if not success:
    if attempt < 3:  
      print('\nSorry, login unsuccessful, please try again\n')
    else:  
      print('\nSorry, that was your third attempt!')
  else:
      break
      
if success:
    print('\nCongratulations, you have sucessfully logged in!')
    '''
# 3 tests: 1. succcessful login 2. unsuccessful 3. 3 attempt termination
# assertion 1:
enter: user2 then ball456
message: Congratulations, you have sucessfully logged in!
# assertion 2 and 3:
enter: user2 then ball
message: Sorry, login unsuccessful, please try again
enter: user then ball456
message: Sorry, login unsuccessful, please try again
enter: user3 then coin8910
message: Sorry, that was your third attempt! - then program terminates
'''
