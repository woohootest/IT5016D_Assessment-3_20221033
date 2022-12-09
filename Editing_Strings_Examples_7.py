# Reversing and inserting characters to a string

# D*l*r*O*w* *o*L*l*E*h 
# @ author: Kat
# date: 15/11/2022


#Strings can be reversed using slicing.

#To reverse a string, create slice that starts

#with the length of the string, and ends at index 0.

string_1 = "Hello World" stringlength=len(string_1) # calculate length of the list

slicedString=string_1[stringlength::-1] # slicing

print (slicedString) # print the reversed string

s='*'.join(string_1)

print(s)
 
Original string is.... 
 
***     xyz     ***
 
Using strip()...
 
*** xyz ***
 
Using lstrip()...
 
*** xyz     ***
 
Using the join method to add a : between every char...
H:e:l:l:o: :W:o:r:l:d 
 
Using the join method to add a whitespace between every char...
H e l l o   W o r l d
