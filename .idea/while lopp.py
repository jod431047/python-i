#wihle loop example
'''
x = 0
while x <= 10 :
    print(x)
    x  +=1
'''
#infinite loop
#Else with while exampel
'''
x = 0
while x <= 10: print(x); x +=1
x = 'jihad'
for letter in x :
    print(letter)
# range(start=0,end ,step=1)
#range(10)             #0 1 2  3 4 5 6 7 8 9
#range(2,10)           #2 3 4 5 6 7 8 9
#range(2,10,2)         #2 4 6 8
'''
'''
for x in range(1,21):
    print(x)
    for x in range(1, 21,2):
        print(x)
'''
'''
for b in range (1,6):
    for y in range(1,11):
        print(b,y)

for x in range (1,6):
    for x in range(1,13):
        print(f"{x} X {y} = {x*y}")
'''
# loop with lists

d = [[1,2,3],[4,5,6]]
for x in d:
     for y in x :
         print(y)