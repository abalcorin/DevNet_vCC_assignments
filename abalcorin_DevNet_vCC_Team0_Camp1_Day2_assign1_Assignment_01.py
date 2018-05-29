"""
Programmability Black Belt Apprentice (Level1)
https://github.com/Devanampriya/DevNet_vCC_Team0/blob/master/Camp1_Day2_assign1
Participant: ALBREN ALCORIN

Assignment
Write a program (in Python 3) to print “I have attended ------ sessions!!” from the below variable dataset containing sessionIDs
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
[hint : it’s a good idea to use the split function]
Eg.
Sessions_Attended = {'sessions' : '1011,2344,'}
Answer:
I have attended 2 sessions!!
"""

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
print('I have attended',len(Sessions_Attended['sessions'].split(',')), 'sessions!!')