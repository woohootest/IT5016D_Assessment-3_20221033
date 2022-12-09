# Returning Data From Functions Practice 2
# author: Kat
# date: 11/11/2022

# Write a short 2 question quiz that uses a function to evaluate each answer
# and return a score.

score = 0
print('\nTwo-item Quiz Example')
def get_score(question, answer, score):
    print('\n'+ question)
    user_response = input('Answer: ')
    if user_response == answer:
        score += 1
        print('Well done')
    else:
        print('Sorry, you got it wrong')
    return score    
score = get_score('What do you call the scope of a variable that can be accessed anywhere 
in the code?', 'global', 0')
score = get_score('What Python statement allows for throwing back of a value used in the 
function to the calling statement?', 'return', score)
print('\nYour score: {0}'.format(score))
'''
# assertion
inputs: global, hello
Two-item Quiz Example
What do you call the scope of a variable that can be accessed anywhere in the code?
Answer: global
Well done
What Python statement allows for throwing back of a value used in the function to the 
calling statement?
Answer: hello
Sorry, you got it wrong
Your score: 1
'''
